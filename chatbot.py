import ollama
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def get_response(messages):
    response = ollama.chat(
        model= "gemma3:1b",
        messages=messages
    )

    return response["message"]["content"]