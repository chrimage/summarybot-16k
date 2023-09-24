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

import subprocess

def remove_silence(audio_file):
    """Remove silence from the audio file using ffmpeg."""
    output_file = audio_file.replace('.m4a', '_no_silence.webm')
    if os.path.exists(output_file):
        print(f"No-silence file already exists at: {output_file}")
    else:
        command = f"ffmpeg -i {audio_file} -af silenceremove=stop_periods=-1:stop_duration=0:start_threshold=0.01:stop_threshold=0.01 -ac 1 -ab 24k -c:a libopus {output_file}"
        subprocess.call(command, shell=True)
        print(f"No-silence file created at: {output_file}")
    return output_file

def download_and_check_audio(video_url, video_title):
    """Download audio from YouTube video, remove silence and check if the file exists."""
    audio_file = download_youtube_audio(video_url, video_title)
    if audio_file is None or not os.path.exists(audio_file):
        print(f"Failed to download audio for {url}")
        return None
    audio_file_no_silence = remove_silence(audio_file)
    return audio_file_no_silence
