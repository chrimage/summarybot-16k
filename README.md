# YouTube Video Summarizer

This application uses OpenAI APIs to summarize YouTube videos. It downloads the audio stream of a YouTube video, transcribes the audio to text, and then summarizes the text transcript.

## Features

- Downloads the audio stream of a YouTube video using the `pytube` library.
- Transcribes the audio to text using OpenAI's Whisper ASR system.
- Summarizes the text transcript using LangChain to prompt OpenAI's GPT-3.5 Turbo.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- OpenAI API key

### Installation

1. Clone the repository: `git clone https://github.com/your_username_/Project-Name.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Create a `.env` file in the project root directory and add your OpenAI API key to it like this: `OPENAI_API_KEY=your_api_key_here`. This project uses the `dotenv` library to load this key into the environment variables.

### Usage

To summarize a YouTube video, run the following command: `python summarize.py {youtube_url}`

The audio file, transcript, and summary will be saved to the `/audio`, `/transcripts`, and `/summaries` folders respectively.

## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for how to contribute.

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for more details.
