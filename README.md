# YouTube Video Summarizer

This application summarizes YouTube videos using OpenAI APIs.

## Overview

The summarizer follows a 3-step process:

1. Downloads the audio stream of a YouTube video using **pytube**

2. Transcribes the audio to text using **OpenAI Whisper**

3. Summarizes the text transcript using **LangChain** to prompt **GPT-3.5 Turbo**

## Usage

To use the summarizer:

1. Clone the repository
2. Install dependencies (`pip install -r requirements.txt`)
3. Add OpenAI API key to `.env` file
4. Run `python summarize.py {youtube_url}`

The audio file, transcript, and summary will be saved to the `/audio`, `/transcripts`, and `/summaries` folders respectively.

## Implementation Details

- **pytube** to download YouTube videos
- **OpenAI Whisper** transcribes audio to text
- **LangChain** sequences calls to **GPT-3.5 Turbo** for summarization

## Contributing

Pull requests are welcome! Potential areas of contribution:

- Support additional video sources
- Improve summarization quality
- Add tests

## License

This project is licensed under the MIT license - see [LICENSE](LICENSE) for more details.