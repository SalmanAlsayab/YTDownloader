import yt_dlp 

# The YouTube URL you want to download
video_url = "https://www.youtube.com/watch?v=Qa-7iWxDz1A"


# Configuration options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    # Saves file as 'Video Title.extension' in the current folder
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': True,
    
    'extractor_args': {
        'youtube': {
            'skip': ['dash', 'hls'],  # Skip DASH and HLS formats
            'player_client': ['android'],  # Use Android client
        },
        'generic': {
            'timeout': ['30'],  # Custom timeout
        }
    },
    
}

# Execute download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url,download=False, ie_key='Youtube')

print(f"{info['thumbnails'][0]['url']}")
print(f"{info['title']}")
print(f"{info['formats'][0]}")