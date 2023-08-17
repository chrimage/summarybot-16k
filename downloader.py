from pytube import YouTube
from slugify import slugify
import os


def download_and_check_audio(url):
    """Download audio from YouTube video and check if the file exists."""
    audio_file = download_youtube_audio(url)
    if audio_file is None or not os.path.exists(audio_file):
        print(f"Failed to download audio for {url}")
        return None
    return audio_file
