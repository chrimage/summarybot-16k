import os
from transcriber import transcribe_video
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

def summarize_video(video_url: str):
    transcript_path = transcribe_video(video_url)
    with open(transcript_path, "r") as f:
        transcript = f.read()
    chat = ChatOpenAI(temperature=1.0,model="gpt-3.5-turbo-16k",openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    system_message_file = "system_message.txt"
    if os.path.exists(system_message_file):
        with open(system_message_file, "r") as f:
            system_message_content = f.read()
    else:
        system_message_content = "You are a YouTube video summarizer. You will be provided with a transcript of the video. Please reply with a detailed summary of the video."
    
    messages = [
        SystemMessage(content=system_message_content),
        HumanMessage(content=transcript)
    ]
    response = chat(messages)
    summary = response.content
    from utils import ensure_directory_exists

    # Create summaries folder if it doesn't exist
    summaries_folder = "summaries"
    ensure_directory_exists(summaries_folder)
    # Save summary to file. We replace the transcript file's extension with .txt
    video_title = download_youtube_audio(video_url).title
    summary_filename = video_title + "-summary.txt"
    summary_path = os.path.join(summaries_folder, summary_filename)
    if not os.path.exists(summary_path):
        print("Summarizing transcript...")
        with open(summary_path, "w") as f:
            f.write(summary)
        print("Summary completed.")
    return summary_path
