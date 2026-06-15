"""YouTube downloader module for downloading videos at various resolutions."""

from pydantic import BaseModel, Field
import yt_dlp


class YDLConfig(BaseModel):
    """Pydantic model for validating yt-dlp configuration options."""

    format: str = Field(..., description="Video format specification")
    ffmpeg_location: str = Field(
        default=r"src\youtube_video_downloader\bin",
        description="location of ffmpeg executables",
    )
    postprocessors: list = Field(
        default_factory=list, description="List of post-processors"
    )
    outtmpl: str = Field(
        default="%(title)s.%(ext)s", description="Output template for downloaded files"
    )
    quiet: bool = Field(default=True, description="Suppress output messages")


def set_format(resolution: str) -> str:
    """set format based on resolution in xxxp format or put 'audio' for audio only format"""

    format_map = {
        "audio": "139/bestaudio/best",
        "1440p": "400+bestaudio[ext=m4a]/bestvideo[height<=1440][ext=mp4]+bestaudio[ext=m4a]",
        "1080p": "137+bestaudio[ext=m4a]/bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]",
        "720p": "136+bestaudio[ext=m4a]/bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]",
        "480p": "135+bestaudio[ext=m4a]/bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]",
        "360p": "134+bestaudio[ext=m4a]/bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]",
    }
    return format_map.get(resolution, "best")


def download_video(url: str, resolution: str) -> None:
    """Download youtube video with specific resolution.

    Args:
        url: Youtube video URL
        resolution: wanted resolution in xxxxp format
    """

    ydl_opts = YDLConfig(format=set_format(resolution))
    with yt_dlp.YoutubeDL(dict(ydl_opts)) as ydl:
        ydl.download(url)


def download_audio_mp3(url: str, output_dir: str = "audio") -> None:
    """Download audio from YouTube video and convert to MP3.

    Args:
        url: YouTube video URL
        output_dir: Directory to save the MP3 file (async default: 'audio')
    """
    # Configure yt-dlp options for audio extraction
    ydl_opts = YDLConfig(
        format=set_format("audio"),
        postprocessors=[
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        outtmpl=f"{output_dir}/%(title)s.%(ext)s",
    )
    # Download and convert the video to MP3
    with yt_dlp.YoutubeDL(dict(ydl_opts)) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    # Example: Download a video at 1080p resolution
    download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", resolution="1080p")
