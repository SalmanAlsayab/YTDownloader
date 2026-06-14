"""YouTube Video Downloader - A simple YouTube video downloader."""

__version__ = "0.1.0"
__author__ = "YTDownloader Contributors"

from .downloader import *  # noqa: F401, F403
from .list_formats import *  # noqa: F401, F403
from .video_info import *  # noqa: F401, F403

__all__ = [
    "downloader",
    "list_formats",
    "video_info",
]
