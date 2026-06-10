import asyncio
from pytubefix import AsyncYouTube

URL = "https://www.youtube.com/watch?v=Qa-7iWxDz1A"

async def main():
    # Initialize AsyncYouTube with OAuth to handle age-restricted content
    yt = AsyncYouTube(URL, use_oauth=True, allow_oauth_cache=True)
    
    # Fetch all available streams asynchronously
    streams = await yt.streams()
    print("Available Streams:")
    for stream in streams:
        print(stream)

if __name__ == '__main__':
    asyncio.run(main())