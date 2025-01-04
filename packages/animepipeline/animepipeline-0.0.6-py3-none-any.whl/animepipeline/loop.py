import asyncio
from pathlib import Path
from typing import Any, Callable, Coroutine, List, Optional

from loguru import logger
from pydantic import DirectoryPath

from animepipeline.bt import QBittorrentManager
from animepipeline.config import NyaaConfig, RSSConfig, ServerConfig
from animepipeline.encode import FinalRipClient
from animepipeline.mediainfo import FileNameInfo, rename_file
from animepipeline.pool import AsyncTaskExecutor
from animepipeline.post import TGChannelSender
from animepipeline.rss import TorrentInfo, parse_nyaa
from animepipeline.store import AsyncJsonStore, TaskStatus
from animepipeline.template import PostTemplate, get_telegram_text


class TaskInfo(TorrentInfo):
    download_path: DirectoryPath
    uploader: str
    script_content: str
    param_content: str
    slice: Optional[bool] = True
    timeout: Optional[int] = 20
    queue: Optional[str] = "priority"


def build_task_info(
    torrent_info: TorrentInfo, nyaa_config: NyaaConfig, rss_config: RSSConfig, server_config: ServerConfig
) -> TaskInfo:
    """
    Build TaskInfo from TorrentInfo, NyaaConfig and RSSConfig

    :param torrent_info: TorrentInfo
    :param nyaa_config: NyaaConfig
    :param rss_config: RSSConfig
    :param server_config: ServerConfig
    :return: TaskInfo
    """
    if nyaa_config.script not in rss_config.scripts:
        raise ValueError(f"script not found: {nyaa_config.script}")
    if nyaa_config.param not in rss_config.params:
        raise ValueError(f"param not found: {nyaa_config.param}")

    script_content = rss_config.scripts[nyaa_config.script]
    param_content = rss_config.params[nyaa_config.param]

    return TaskInfo(
        **torrent_info.model_dump(),
        download_path=server_config.qbittorrent.download_path,
        uploader=nyaa_config.uploader,
        script_content=script_content,
        param_content=param_content,
        slice=nyaa_config.slice,
        timeout=nyaa_config.timeout,
        queue=nyaa_config.queue,
    )


class Loop:
    """
    Loop: main loop for animepipeline

    :param server_config: an instance of ServerConfig
    :param rss_config: an instance of RSSConfig
    :param json_store: an instance of AsyncJsonStore
    """

    def __init__(self, server_config: ServerConfig, rss_config: RSSConfig, json_store: AsyncJsonStore):
        self.stop_event = asyncio.Event()

        self.server_config = server_config
        self.rss_config = rss_config

        self.json_store = json_store

        self.task_executor = AsyncTaskExecutor()  # async task pool

        self.qbittorrent_manager = QBittorrentManager(config=self.server_config.qbittorrent)

        self.finalrip_client = FinalRipClient(config=self.server_config.finalrip)

        self.tg_channel_sender = (
            TGChannelSender(config=self.server_config.telegram) if self.server_config.telegram.enable else None
        )

        self.pipeline_tasks: List[Callable[[TaskInfo], Coroutine[Any, Any, None]]] = []
        self.add_pipeline_task()

    async def stop(self) -> None:
        """
        Stop the loop
        """
        self.stop_event.set()
        await self.task_executor.shutdown()
        logger.warning("Loop stopped successfully!")

    async def start(self) -> None:
        """
        Start the loop
        """
        while not self.stop_event.is_set():
            # refresh rss config
            self.rss_config.refresh_config()
            for cfg in self.rss_config.nyaa:
                try:
                    torrent_info_list = parse_nyaa(cfg)
                except Exception as e:
                    logger.error(f"Failed to parse nyaa for {cfg.name}: {e}")
                    continue

                for torrent_info in torrent_info_list:
                    task_info = build_task_info(
                        torrent_info=torrent_info,
                        nyaa_config=cfg,
                        rss_config=self.rss_config,
                        server_config=self.server_config,
                    )

                    await self.task_executor.submit_task(torrent_info.hash, self.pipeline, task_info)

            await asyncio.sleep(self.server_config.loop.interval)

    def add_pipeline_task(self) -> None:
        """
        Add pipeline task to the loop

        """
        self.pipeline_tasks.append(self.pipeline_bt)
        self.pipeline_tasks.append(self.pipeline_finalrip)
        self.pipeline_tasks.append(self.pipeline_post)

    async def pipeline(self, task_info: TaskInfo) -> None:
        # init task status
        if not await self.json_store.check_task_exist(task_info.hash):
            await self.json_store.add_task(task_id=task_info.hash, status=TaskStatus())

        task_status = await self.json_store.get_task(task_info.hash)
        if task_status.done:
            return

        logger.info(f'Start pipeline for "{task_info.name}" EP {task_info.episode}')

        # pipeline tasks
        for pipeline_task in self.pipeline_tasks:
            await pipeline_task(task_info)

        # Done!
        task_status = await self.json_store.get_task(task_info.hash)  # update task_status!!!!!!!!
        task_status.done = True
        await self.json_store.update_task(task_info.hash, task_status)
        logger.info(f'Finish pipeline for "{task_info.name}" EP {task_info.episode}')

    async def pipeline_bt(self, task_info: TaskInfo) -> None:
        task_status = await self.json_store.get_task(task_info.hash)

        # check bt
        if task_status.bt_downloaded_path is not None:
            return

        logger.info(f'Start BT download for "{task_info.name}" EP {task_info.episode}')
        # download torrent file
        while not self.qbittorrent_manager.check_torrent_exist(task_info.hash):
            self.qbittorrent_manager.add_torrent(torrent_hash=task_info.hash, torrent_url=task_info.link)  # type: ignore
            await asyncio.sleep(10)

        # check download complete
        while not self.qbittorrent_manager.check_download_complete(task_info.hash):
            await asyncio.sleep(10)

        # get downloaded path
        bt_downloaded_path = self.qbittorrent_manager.get_downloaded_path(task_info.hash)

        # update task status
        task_status.bt_downloaded_path = str(bt_downloaded_path)
        await self.json_store.update_task(task_info.hash, task_status)

    async def pipeline_finalrip(self, task_info: TaskInfo) -> None:
        task_status = await self.json_store.get_task(task_info.hash)

        # check finalrip
        if task_status.finalrip_downloaded_path is not None:
            return

        if task_status.bt_downloaded_path is None:
            logger.error("BT download path is None! bt download task not finished?")
            raise ValueError("BT download path is None! bt download task not finished?")

        logger.info(f'Start FinalRip Encode for "{task_info.name}" EP {task_info.episode}')
        # start finalrip task

        bt_downloaded_path = Path(task_info.download_path) / task_status.bt_downloaded_path

        while not await self.finalrip_client.check_task_exist(bt_downloaded_path.name):
            try:
                await self.finalrip_client.upload_and_new_task(bt_downloaded_path)
                logger.info(f'FinalRip Task Created for "{task_info.name}" EP {task_info.episode}')
            except Exception as e:
                logger.error(f"Failed to upload and new finalrip task: {e}")
            await asyncio.sleep(10)

        try:
            await self.finalrip_client.start_task(
                video_key=bt_downloaded_path.name,
                encode_param=task_info.param_content,
                script=task_info.script_content,
                slice=task_info.slice,
                timeout=task_info.timeout,
                queue=task_info.queue,
            )
            logger.info(f'FinalRip Task Started for "{task_info.name}" EP {task_info.episode}')
        except Exception as e:
            logger.error(f"Failed to start FinalRip task: {e}")

        # check task progress
        while not await self.finalrip_client.check_task_completed(bt_downloaded_path.name):
            await asyncio.sleep(30)
        logger.info(f'FinalRip encode task completed for "{task_info.name}" EP {task_info.episode}')

        # download temp file to bt_downloaded_path's parent directory
        temp_saved_path: Path = bt_downloaded_path.parent / (bt_downloaded_path.name + "-encoded.mkv")
        await self.finalrip_client.download_completed_task(video_key=bt_downloaded_path.name, save_path=temp_saved_path)

        # rename temp file
        try:
            finalrip_downloaded_path = rename_file(
                FileNameInfo(
                    path=temp_saved_path,
                    episode=task_info.episode,
                    name=task_info.name,
                    uploader=task_info.uploader,
                    type="WEBRip",
                )
            )
        except Exception as e:
            logger.error(f"Failed to generate file name: {e}")
            raise e

        logger.info(f'FinalRip Encode Done for "{finalrip_downloaded_path.name}"')

        # update task status
        task_status.finalrip_downloaded_path = finalrip_downloaded_path.name
        await self.json_store.update_task(task_info.hash, task_status)

    async def pipeline_post(self, task_info: TaskInfo) -> None:
        task_status = await self.json_store.get_task(task_info.hash)

        # check posted
        if task_status.posted:
            return

        if task_status.finalrip_downloaded_path is None:
            logger.error("FinalRip download path is None! finalrip download task not finished?")
            raise ValueError("FinalRip download path is None! finalrip download task not finished?")

        finalrip_downloaded_path = Path(task_info.download_path) / task_status.finalrip_downloaded_path
        torrent_file_save_path = Path(task_info.download_path) / (str(finalrip_downloaded_path.name) + ".torrent")

        try:
            torrent_file_hash = QBittorrentManager.make_torrent_file(
                file_path=finalrip_downloaded_path,
                torrent_file_save_path=torrent_file_save_path,
            )
            logger.info(f"Torrent file created: {torrent_file_save_path}, hash: {torrent_file_hash}")
        except Exception as e:
            logger.error(f"Failed to create torrent file: {e}")
            raise e

        self.qbittorrent_manager.add_torrent(torrent_hash=torrent_file_hash, torrent_file_path=torrent_file_save_path)

        logger.info(f"Generate all post info files for {task_info.name} EP {task_info.episode} ...")

        try:
            post_template = PostTemplate(
                video_path=finalrip_downloaded_path,
                bangumi_url=task_info.bangumi,  # type: ignore
                chinese_name=task_info.translation,
                uploader="TensoRaws",
            )

            post_template.save(
                html_path=Path(task_info.download_path) / (finalrip_downloaded_path.name + ".html"),
                markdown_path=Path(task_info.download_path) / (finalrip_downloaded_path.name + ".md"),
                bbcode_path=Path(task_info.download_path) / (finalrip_downloaded_path.name + ".txt"),
            )
        except Exception as e:
            logger.error(f"Failed to generate post info files: {e}")

        logger.info(f"Post to Telegram Channel for {task_info.name} EP {task_info.episode} ...")

        if self.tg_channel_sender is None:
            logger.info("Telegram Channel Sender is not enabled. Skip upload.")
        else:
            tg_text = get_telegram_text(
                chinese_name=task_info.translation,
                episode=task_info.episode,
                file_name=finalrip_downloaded_path.name,
                torrent_file_hash=torrent_file_hash,
            )
            await self.tg_channel_sender.send_text(text=tg_text)

        # update task status
        task_status.posted = True
        await self.json_store.update_task(task_info.hash, task_status)
