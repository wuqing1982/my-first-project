import yt_dlp
import os

def download_youtube_video(url, cookie_file, resolution="1080", file_format="mp4", download_path="."):
    """
    Enhanced YouTube video, thumbnail, and subtitle downloader.
    :param url: YouTube video URL
    :param cookie_file: Path to cookie file
    :param resolution: Desired video resolution, default is "1080"
    :param file_format: Video file format, default is "mp4"
    :param download_path: Local download path, default is current directory
    """
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.youtube.com/'
    }

    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[ext={file_format}]',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'cookiefile': cookie_file,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': file_format
        }],
        'merge_output_format': file_format,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en', 'zh-Hans'],
        'subtitlesformat': 'vtt',  # Changed to 'vtt' as 'srt' may not be available
        'writethumbnail': True,
        'postprocessors': [{
            'key': 'FFmpegThumbnailsConvertor',
            'format': 'jpg',
        }],
        'noplaylist': True,
        'headers': headers,
        'retries': 10,  # Increased retry attempts for unreliable connections
        'socket_timeout': 60  # Increased timeout to avoid premature disconnections
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"Video, thumbnail, and available subtitles successfully downloaded to: {download_path}")
        except Exception as e:
            print(f"Download failed: {e}")

if __name__ == "__main__":
    video_url = input("Please enter YouTube video URL: ").strip()
    cookie_file_path = input("Please enter the path to your cookie file: ").strip() or "www.youtube.com_cookies.txt"
    resolution = input("Please enter resolution (default is 1080): ").strip() or "1080"
    file_format = input("Please enter format (default is mp4): ").strip() or "mp4"
    download_path = input("Please enter download path (default is current directory): ").strip() or "."

    download_youtube_video(video_url, cookie_file_path, resolution, file_format, download_path)
