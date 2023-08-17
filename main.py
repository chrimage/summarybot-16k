from downloader import download_youtube_audio
from transcriber import transcribe_video
from summarizer import summarize_video
import argparse
from typing import Optional

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    # URL is the only input
    parser.add_argument("url")
    args = parser.parse_args()
    video_url = args.url
    print(f"Processing video: {video_url}")
    summary = summarize_video(video_url)
    print(f"Summary saved at: {summary}")
    print(summary)

if __name__ == "__main__":
    main()
