import yt_dlp
import json
def list_formats(url):
    wanted_ext = ['mp4', 'm4a']
    available_formats = {'id': [],
                         'resolustions': [],
                         'ext':[],
                         'size':[]}
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        for fmt in info['formats']:
            filesize = fmt.get('filesize')
            if filesize and (fmt.get('ext') in wanted_ext):
                resolution = f"{fmt.get('width', '?')}x{fmt.get('height', '?')}"
                if resolution not in available_formats['resolustions']:
                    available_formats['resolustions'].append(resolution)
                    available_formats['id'].append(fmt.get('format_id', 'N/A'))
                    available_formats['ext'].append(fmt.get('ext', 'N/A'))
                    size_str = f"{filesize / 1024 / 1024:.1f} MB" if filesize else "N/A"
                    available_formats['size'].append(size_str)
        
    return json.dumps(available_formats, indent=4)
    
if __name__=="__main__":    
    print(list_formats("https://www.youtube.com/watch?v=Qa-7iWxDz1A"))