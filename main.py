from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
import openai
import os
import torch
import json
import requests

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")
openai.organization = os.getenv("OPEN_AI_ORG")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/talk")
async def post_audio(file: UploadFile):
    user_message = transcribe_audio(file)
    chat_response = get_chat_response(user_message)
    return chat_response

# Functions:::
def transcribe_audio(file):
    audio_file = open(file.filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
    return transcript

def get_chat_response(user_message):
    messages = load_messages()
    messages.append({"role": "user", "content": user_message['text']})
    gpt_response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    parsed_gpt_response = gpt_response['choices'][0]['message']['content']
    #send to gpt
    save_messages(user_message['text'], parsed_gpt_response)

    return parsed_gpt_response


def load_messages():
    messages = []
    file = 'database.json'
    
    #check if database.jon file is empty
    empty = os.stat(file).st_size == 0

    if not empty:
        with open(file) as db_file:
            data = json.load(db_file)
            for item in data:
                messages.append(item)
    else:
        messages.append(
                {"role": "system", "content": "You are interviewing the user for a Machine Learning Engineer position. Ask short questions that are relevant to a junior level engineer. Your name is Jarvis. The user is Arush. Keep responses under 30 words."}
                )
    return messages

def save_messages(user_message, gpt_response):
    file = 'database.json'
    messages = load_messages()
    messages.append({"role": "user", "content": user_message})
    messages.append({"role": "assistant", "content": gpt_response})
    with open(file, 'w') as f:
        json.dump(messages, f)
