"""Module for listing available video formats from YouTube."""

from typing import Dict, List, Any, Optional
import json
from pydantic import BaseModel, Field
import yt_dlp


class VideoFormat(BaseModel):
    """Pydantic model for video format information."""

    id: List[str] = Field(description="Format IDs")
    resolutions: List[str] = Field(description="Video resolutions")
    ext: List[str] = Field(description="File extensions")
    size: List[str] = Field(description="File sizes in MB")


def list_formats(url: str) -> str:
    """Retrieve and list all available video formats for a given YouTube URL.

    Args:
        url: YouTube video URL

    Returns:
        JSON string containing available formats with resolutions, sizes, and IDs
    """
    # Only interested in MP4 and M4A formats
    wanted_ext: List[str] = ["mp4", "m4a"]

    # Dictionary to store format information
    available_formats: Dict[str, List[str]] = {
        "id": [],
        "resolutions": [],
        "ext": [],
        "size": [],
    }

    # Configure yt-dlp to extract info without downloading
    ydl_opts: Dict[str, Any] = {
        "quiet": True,
        "skip_download": True,
    }

    # Extract and filter video formats
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info: Dict[str, Any] = ydl.extract_info(url, download=False)

        # Iterate through all available formats
        for fmt in info["formats"]:
            filesize: Optional[int] = fmt.get("filesize")

            # Only process formats with filesize and desired extensions
            if filesize and (fmt.get("ext") in wanted_ext):
                # Create resolution string from width and height
                resolution: str = f"{fmt.get('width', '?')}x{fmt.get('height', '?')}"

                # Add to list if resolution hasn't been added yet
                if resolution not in available_formats["resolutions"]:
                    available_formats["resolutions"].append(resolution)
                    available_formats["id"].append(fmt.get("format_id", "N/A"))
                    available_formats["ext"].append(fmt.get("ext", "N/A"))
                    # Convert filesize to MB
                    size_str: str = (
                        f"{filesize / 1024 / 1024:.1f} MB" if filesize else "N/A"
                    )
                    available_formats["size"].append(size_str)

    return json.dumps(available_formats, indent=4)


if __name__ == "__main__":
    # Example: List all available formats for a YouTube video
    print(list_formats("https://www.youtube.com/watch?v=Qa-7iWxDz1A"))
