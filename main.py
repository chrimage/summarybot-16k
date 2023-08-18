from downloader import download_youtube_audio
from transcriber import transcribe_video
from summarizer import summarize_video
import argparse
from typing import Optional

from utils import get_video_title

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    # URL is the only input
    parser.add_argument("url")
    args = parser.parse_args()
    video_url = args.url
    if not ("youtube" in video_url or "youtu.be" in video_url):
        print("Invalid YouTube URL")
        return

    print(f"Processing video: {video_url}")
    summary = summarize_video(video_url)
    print(f"Summary saved at: {summary}")
    print(summary)

if __name__ == "__main__":
    main()
