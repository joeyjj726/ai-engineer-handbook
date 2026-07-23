from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Hello AI Engineer!"
    }


@app.get("/hello")
def hello():
    return {
        "name": "Joey",
        "job": "AI Engineer"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": request.question
            }
        ],
        "stream": False
    }

    response = requests.post(URL, json=payload)
    response.raise_for_status()

    result = response.json()

    answer = result["message"]["content"]

    return {
        "answer": answer
    }