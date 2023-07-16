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
    chat = ChatOpenAI(temperature=1.0,model="gpt-3.5-turbo-16k")
    messages = [
        SystemMessage(
            content="You are a YouTube video summarizer. You will be provided with a transcript of the video. Please reply with a detailed summary of the video."
            ),
        HumanMessage(content=transcript)
    ]
    response = chat(messages)
    summary = response.content
    # Create summaries folder if it doesn't exist
    summaries_folder = "summaries"
    if not os.path.exists(summaries_folder):
        os.makedirs(summaries_folder)
    # Save summary to file. We replace the transcript file's extension with .txt
    summary_filename = os.path.basename(transcript_path)
    summary_path = os.path.join(summaries_folder, summary_filename)
    with open(summary_path, "w") as f:
        f.write(summary)