from pytube import YouTube
from utils import get_video_title
from slugify import slugify
import os


from urllib.error import HTTPError

def download_youtube_audio(url, video_title):
    """Download audio from YouTube video and return the file path."""
    youtube = YouTube(url)
    audio = youtube.streams.filter(only_audio=True,audio_codec="mp4a.40.5").first()
    filename = slugify(video_title) + '.m4a'
    output_directory = os.path.join(os.getcwd(), 'audio')
    from utils import ensure_directory_exists
    ensure_directory_exists(output_directory)
    output_path = os.path.join(output_directory, filename)
    if os.path.exists(output_path):
        print(f"Audio file already exists at: {output_path}")
    else:
        print(f"Downloading audio from: {url}")
        audio.download(filename=filename, output_path=output_directory)
        print(f"Audio downloaded at: {output_path}")
    return output_path


def download_and_check_audio(video_url, video_title):
    """Download audio from YouTube video and check if the file exists."""
    audio_file = download_youtube_audio(video_url, video_title)
    if audio_file is None or not os.path.exists(audio_file):
        print(f"Failed to download audio for {url}")
        return None
    return audio_file
