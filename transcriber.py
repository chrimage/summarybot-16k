from downloader import download_youtube_audio
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def check_transcript_exists(audio_file):
    """Check if transcript file already exists."""
    base_filename, _ = os.path.splitext(os.path.basename(audio_file))
    transcript_filename = base_filename + ".txt"
    transcript_path = os.path.join("transcripts", transcript_filename)
    if os.path.exists(transcript_path):
        print(f"Transcript file already exists for {audio_file}")
        return transcript_path
    return None

def transcribe_audio(audio_file):
    """Transcribe audio file."""
    base_filename, _ = os.path.splitext(os.path.basename(audio_file))
    transcript_filename = base_filename + ".txt"
    transcript_path = os.path.join("transcripts", transcript_filename)
    with open(audio_file, "rb") as f:
        try:
            transcript = openai.Audio.transcribe("whisper-1", f)
        except Exception as e:
            print(f"Failed to transcribe audio for {audio_file}: {e}")
            return None
    with open(transcript_path, "w") as f:
        f.write(transcript['text'])
    return transcript_path

def transcribe_video(video_url: str):
    """Download audio, check if transcript exists, and transcribe audio."""
    from downloader import download_and_check_audio
    audio_file = download_and_check_audio(video_url)
    if audio_file is None:
        return None
    transcript_path = check_transcript_exists(audio_file)
    if transcript_path is not None:
        return transcript_path
    return transcribe_audio(audio_file)
