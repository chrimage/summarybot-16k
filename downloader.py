from pytube import YouTube
from slugify import slugify
import os


def download_youtube_audio(url):
    # Create YouTube object
    yt = YouTube(url)

    # Get highest quality audio stream
    video = yt.streams.filter(only_audio=True).first()

    # Slugify the title
    filename = slugify(yt.title)

    # Make sure the ./audio/ directory exists
    audio_directory = "./audio/"
    if not os.path.exists(audio_directory):
        os.makedirs(audio_directory)

    # Download the audio
    out_file = video.download(output_path=audio_directory, filename=filename)

    # Rename the file to have .mp3 extension
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print(new_file)

    # Return the new file path
    return new_file



