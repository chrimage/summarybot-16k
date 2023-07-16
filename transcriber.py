from downloader import download_youtube_audio
import openai
import os
from dotenv import load_dotenv
load_dotenv()

def transcribe_video(video_url: str):
    # Download audio
    audio_file = download_youtube_audio(video_url)

    if audio_file is None or not os.path.exists(audio_file):
        print(f"Failed to download audio for {video_url}")
        return None

    # Check if transcript file already exists
    base_filename, _ = os.path.splitext(os.path.basename(audio_file))
    transcript_filename = base_filename + ".txt"
    transcript_path = os.path.join("transcripts", transcript_filename)

    if os.path.exists(transcript_path):
        print(f"Transcript file already exists for {video_url}")
        return transcript_path

    # Open the audio file
    with open(audio_file, "rb") as f:
        try:
            transcript = openai.Audio.transcribe("whisper-1", f)
        except Exception as e:
            print(f"Failed to transcribe audio for {video_url}: {e}")
            return None

    # Save transcript to file
    with open(transcript_path, "w") as f:
        f.write(transcript['text'])

    return transcript_path