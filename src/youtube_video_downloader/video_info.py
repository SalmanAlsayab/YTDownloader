"""Module for extracting video metadata like thumbnails and titles from YouTube."""

from typing import Dict, Any
import json
from pydantic import BaseModel, Field
import yt_dlp


class VideoMetadata(BaseModel):
    """Pydantic model for video metadata."""

    thumbnails: str = Field(None, description="Thumbnail URL")
    title: str = Field(None, description="Video title")


async def thumbnail_title(url: str) -> str:
    """Extract thumbnail URL and title from a YouTube video.

    Args:
        url: YouTube video URL

    Returns:
        JSON string containing video title and thumbnail URL
    """

    # Configuration options for yt-dlp
    ydl_opts: Dict[str, Any] = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",  # Output filename template
        "quiet": True,
        "skip_download": True,  # Only extract info, don't download
        "extractor_args": {
            "youtube": {
                "skip": [
                    "dash",
                    "hls",
                ],  # Skip DASH and HLS formats for faster extraction
                "player_client": [
                    "android"
                ],  # Use Android client for better compatibility
            },
            "generic": {
                "timeout": ["30"],  # 30 second timeout for generic extractors
            },
        },
    }

    # Extract video information without downloading the file
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info: Dict[str, Any] = ydl.extract_info(url, download=False, ie_key="Youtube")
        meta_data = VideoMetadata(thumbnails=info["thumbnail"], title=info["title"])

    return json.dumps(dict(meta_data), indent=4)


if __name__ == "__main__":
    # Example: Extract metadata from a YouTube video
    video_url: str = "https://www.youtube.com/watch?v=Qa-7iWxDz1A"
    print(thumbnail_title(video_url))
