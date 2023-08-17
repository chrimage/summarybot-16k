import os

def ensure_directory_exists(directory):
    """Ensure that a directory exists. If it doesn't, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
from pytube import YouTube
from slugify import slugify

def get_video_title(url):
    """Get the title of the YouTube video."""
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    return slugify(video.title)
