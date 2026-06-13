import yt_dlp 
import json


def thumbnail_title(url):
    video_info = {}

    # Configuration options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        # Saves file as 'Video Title.extension' in the current folder
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'skip_download':True,
        
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
        video_info['thumbnails'] = info['thumbnail']
        video_info['title'] = info['title']    
    return json.dumps(video_info, indent=4)

if __name__=="__main__":
    video_url = "https://www.youtube.com/watch?v=Qa-7iWxDz1A"
    print(thumbnail_title(video_url))    
