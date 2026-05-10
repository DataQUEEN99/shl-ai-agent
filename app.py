
from services.llm_service import generate_reply
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from services.retrieval import search_assessments

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/")
def home():
    return {"message": "Server working"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.messages[-1].content

    recommendations = search_assessments(user_message)

    reply = generate_reply(user_message, recommendations)

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }