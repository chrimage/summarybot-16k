from pytube import YouTube
from slugify import slugify
import os


def download_youtube_audio(url):
    """Download audio from YouTube video."""
    # Create YouTube object
    youtube_video = YouTube(url)

    # Get highest quality audio stream
    audio_stream = youtube_video.streams.filter(only_audio=True).first()

    # Slugify the title
    title = youtube_video.title
    slugified_title = slugify(title)
    filename = slugified_title + ".mp3"

    from utils import ensure_directory_exists

    # Make sure the ./audio/ directory exists
    audio_directory = "./audio/"
    ensure_directory_exists(audio_directory)

    # If the file already exists, return the file path
    if os.path.isfile(audio_directory + filename):
        return audio_directory + filename

    # If the file does not exist, download it
    elif not os.path.isfile(audio_directory + filename):
        print("Downloading audio...")  # Download the audio
        out_file = audio_stream.download(output_path=audio_directory, filename=filename)
        return out_file
