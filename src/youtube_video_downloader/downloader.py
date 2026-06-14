"""YouTube downloader module for downloading videos at various resolutions."""

from typing import Dict, Any
from asyncio import run
from pydantic import BaseModel, Field
import yt_dlp


class YDLConfig(BaseModel):
    """Pydantic model for validating yt-dlp configuration options."""

    format: str = Field(..., description="Video format specification")
    postprocessors: list = Field(
        default_factory=list, description="List of post-processors"
    )
    outtmpl: str = Field(..., description="Output template for downloaded files")
    quiet: bool = Field(default=False, description="Suppress output messages")


async def download_audio_mp3(url: str, output_dir: str = "audio") -> None:
    """Download audio from YouTube video and convert to MP3.

    Args:
        url: YouTube video URL
        output_dir: Directory to save the MP3 file (async default: 'audio')
    """
    # Configure yt-dlp options for audio extraction
    ydl_opts: Dict[str, Any] = {
        "format": "139/bestaudio/best",
        "ffmpeg_location": r"src\youtube_video_downloader\bin",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "quiet": False,
    }

    # Download and convert the video to MP3
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


async def download_1440p(url: str) -> None:
    """Download video at 1440p resolution (2K).

    Args:
        url: YouTube video URL
    """
    # Configure format for 1440p video with best audio
    ydl_opts: Dict[str, Any] = {
        "ffmpeg_location": r"src\youtube_video_downloader\bin",
        "format": "400+bestaudio[ext=m4a]/bestvideo[height<=1440][ext=mp4]+bestaudio[ext=m4a]",
        "outtmpl": "%(title)s.%(ext)s",
    }

    # Execute the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


async def download_1080p(url: str) -> None:
    """Download video at 1080p resolution (Full HD).

    Args:
        url: YouTube video URL
    """
    # Configure format for 1080p video with best audio
    ydl_opts: Dict[str, Any] = {
        "ffmpeg_location": r"src\youtube_video_downloader\bin",
        "format": "137+bestaudio[ext=m4a]/bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]",
        "outtmpl": "%(title)s.%(ext)s",
    }

    # Execute the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


async def download_720p(url: str) -> None:
    """Download video at 720p resolution (HD).

    Args:
        url: YouTube video URL
    """
    # Configure format for 720p video with best audio
    ydl_opts: Dict[str, Any] = {
        "ffmpeg_location": r"src\youtube_video_downloader\bin",
        "format": "136+bestaudio[ext=m4a]/bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]",
        "outtmpl": "%(title)s.%(ext)s",
    }

    # Execute the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


async def download_480p(url: str) -> None:
    """Download video at 480p resolution (SD).

    Args:
        url: YouTube video URL
    """
    # Configure format for 480p video with best audio
    ydl_opts: Dict[str, Any] = {
        "ffmpeg_location": r"src\youtube_video_downloader\bin",
        "format": "135+bestaudio[ext=m4a]/bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]",
        "outtmpl": "%(title)s.%(ext)s",
    }

    # Execute the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


async def download_360p(url: str) -> None:
    """Download video at 360p resolution (nHD).

    Args:
        url: YouTube video URL
    """
    # Configure format for 360p video with best audio
    ydl_opts: Dict[str, Any] = {
        "ffmpeg_location": r"src\youtube_video_downloader\bin",
        "format": "134+bestaudio[ext=m4a]/bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]",
        "outtmpl": "%(title)s.%(ext)s",
    }

    # Execute the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    # Example: Download a video at 1080p resolution
    run(download_audio_mp3("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
