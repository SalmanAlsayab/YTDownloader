import yt_dlp 

# The YouTube URL you want to download
video_url = "https://www.youtube.com/watch?v=Qa-7iWxDz1A"

# Configuration options
ydl_opts = {
    # 'bestvideo+bestaudio' requests highest quality streams
    # 'best' acts as a fallback if ffmpeg is missing
    'format': 'bestvideo+bestaudio/best',
    # Saves file as 'Video Title.extension' in the current folder
    'outtmpl': '%(title)s.%(ext)s', 
}

# Execute download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download complete!")
