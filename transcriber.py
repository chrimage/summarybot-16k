from downloader import download_youtube_audio
from utils import get_video_title
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_transcript_filename_and_path(video_title, video_url):
    """Get the transcript filename and path."""
    transcript_filename = video_title + "-transcript.txt"
    transcript_path = os.path.join("transcripts", transcript_filename)
    return transcript_filename, transcript_path

def check_transcript_exists(audio_file, video_url):
    """Check if transcript file already exists."""
    video_title = get_video_title(video_url)
    _, transcript_path = get_transcript_filename_and_path(video_title, video_url)
    if os.path.exists(transcript_path):
        print(f"Transcript file already exists for {audio_file}")
        return transcript_path
    return None

def transcribe_audio(audio_file):
    """Transcribe audio file."""
    video_title = get_video_title(video_url)
    _, transcript_path = get_transcript_filename_and_path(video_title)
    with open(audio_file, "rb") as f:
        try:
            transcript = openai.Audio.transcribe("whisper-1", f)
        except Exception as e:
            print(f"Failed to transcribe audio for {audio_file}: {e}")
            return None
    with open(transcript_path, "w") as f:
        print(f"Transcribing audio from: {audio_file}")
        f.write(transcript['text'])
        print(f"Transcript saved at: {transcript_path}")
    return transcript_path

def transcribe_video(video_url: str, video_title: str):
    """Download audio, check if transcript exists, and transcribe audio."""
    from downloader import download_and_check_audio
    audio_file = download_and_check_audio(video_url, video_title)
    if audio_file is None:
        return None
    transcript_path = check_transcript_exists(audio_file, video_title)
    if transcript_path is not None:
        return transcript_path
    return transcribe_audio(audio_file, video_title)
