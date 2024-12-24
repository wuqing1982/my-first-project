import yt_dlp
import os

def download_single_youtube_video():
    """
    Download a single YouTube video to a specified path with given resolution and format after prompting user for details.
    """
    # User input for the video URL
    video_url = input("Please enter YouTube video URL: ").strip()
    
    # User input for the download path with default option
    download_path = input("Please enter download path (default is current directory): ").strip() or "."
    
    # User input for the video resolution with default option
    resolution = input("Please enter resolution (default is 1080): ").strip() or "1080"
    
    # User input for the file format with default option
    file_format = input("Please enter format (default is mp4): ").strip() or "mp4"
    
    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Options for yt_dlp
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[ext={file_format}]',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'merge_output_format': file_format,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'vtt',
        'writethumbnail': True,
        'retries': 10,
        'socket_timeout': 60
    }

    # Download process with error handling
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"Video successfully downloaded to: {download_path}")
        except Exception as e:
            print(f"Download failed: {e}")

# Calling the function to execute the download
download_single_youtube_video()
