from pytube import YouTube
from utils import get_video_title
from slugify import slugify
import os


def download_youtube_audio(url, video_url):
    """Download audio from YouTube video and return the file path."""
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    filename = slugify(video.title) + '.webm'
    output_path = os.path.join(os.getcwd(), 'audio', filename)
    from utils import ensure_directory_exists
    ensure_directory_exists('audio')
    if os.path.exists(output_path):
        print(f"Audio file already exists at: {output_path}")
    else:
        print(f"Downloading audio from: {url}")
        output_path = video.download(filename=filename, output_path=output_path)
        print(f"Audio downloaded at: {output_path}")
    return output_path


def download_and_check_audio(video_url):
    """Download audio from YouTube video and check if the file exists."""
    audio_file = download_youtube_audio(video_url, video_url)
    if audio_file is None or not os.path.exists(audio_file):
        print(f"Failed to download audio for {url}")
        return None
    return audio_file
