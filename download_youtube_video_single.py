import yt_dlp
import os


def download_youtube_video(url, cookie_file, resolution="1080", file_format="mp4", download_path="."):
    """
    下载 YouTube 视频、封面图片和字幕。
    :param url: 视频网址
    :param cookie_file: 带路径的 Cookie 文件
    :param resolution: 分辨率，默认为 "1080"
    :param file_format: 格式，默认为 "mp4"
    :param download_path: 下载路径，默认为当前目录 "."
    """
    # 检查下载路径是否存在
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # 设置自定义的 headers（User-Agent 和 Referer）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.youtube.com/'
    }

    # 设置 yt_dlp 的选项
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[ext={file_format}]',  # 设置分辨率和格式
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # 保存路径和文件名模板
        'cookiefile': cookie_file,  # 使用提供的 Cookie 文件
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': file_format  # 设置视频转换为指定格式
        }],
        'merge_output_format': file_format,  # 合并视频和音频为指定格式
        'writesubtitles': True,  # 下载字幕
        'writeautomaticsub': True,  # 下载自动生成的字幕
        'subtitleslangs': ['en', 'zh-Hans'],  # 下载英文和简体中文字幕
        'subtitlesformat': 'srt',  # 字幕格式为 srt
        'writethumbnail': True,  # 下载封面图片
        'postprocessors': [{
            'key': 'FFmpegThumbnailsConvertor',
            'format': 'jpg',  # 将封面图片转换为 jpg 格式
        }],
        'noplaylist': True,  # 强制只下载单个视频，避免下载播放列表
        'headers': headers  # 自定义 headers
    }
    
    # 执行下载
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"视频、封面图片和可用字幕已成功下载到目录: {download_path}")
        except Exception as e:
            print(f"下载失败: {e}")

# 主函数部分
if __name__ == "__main__":
    # 输入参数
    video_url = input("请输入 YouTube 视频网址: ").strip()
    cookie_file_path = input("请输入带路径的 Cookie 文件路径: ").strip() or "www.youtube.com_cookies.txt"
    resolution = input("请输入分辨率 (默认为1080): ").strip() or "1080"
    file_format = input("请输入格式 (默认为 mp4): ").strip() or "mp4"
    download_path = input("请输入下载的本地路径 (默认为当前目录): ").strip() or "."

    # 下载视频
    download_youtube_video(video_url, cookie_file_path, resolution, file_format, download_path)
