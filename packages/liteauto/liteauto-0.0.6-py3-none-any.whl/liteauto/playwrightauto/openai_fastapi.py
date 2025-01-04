import asyncio
import json
import uuid
import datetime
from typing import Optional, Dict, Any, List

import uvicorn
from fastapi import FastAPI, HTTPException, Header, Request, WebSocket
from pydantic import BaseModel, Field

from liteauto.playwrightauto._oai import ChatHFClient
from fastapi.responses import StreamingResponse

hf_client = None
app = FastAPI(title="OpenAI Compatible API")

def init_hf_client():
    global hf_client
    hf_client = ChatHFClient()

# Models for request/response validation
class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    stream: Optional[bool] = False
    temperature: Optional[float] = 1.0
    max_tokens: Optional[int] = None


class ImageGenerationRequest(BaseModel):
    prompt: str
    model: Optional[str] = "dall-e-2"
    n: Optional[int] = 1
    size: Optional[str] = "1024x1024"


class EmbeddingRequest(BaseModel):
    input: str
    model: Optional[str] = "text-embedding-ada-002"


class ModerationRequest(BaseModel):
    input: str
    model: Optional[str] = "text-moderation-latest"

# Chat Completions endpoint
async def generate_chunks():
    # Simulate streaming responses
    # Replace this with your actual HF client streaming implementation
    chunks = ["Hello", " world", "!", " How", " are", " you", "?"]
    for chunk in chunks:
    # for chunk in hf_client.completions.create(
    #         messages=[
    #             {"role": "user", "content": "tell me about narendra modi in 25 words"}
    #         ],
    #         stream=True,
    #         web_search=False
    #     ):
        response = {
            "id": f"chatcmpl-{uuid.uuid4()}",
            "object": "chat.completion.chunk",
            "created": int(datetime.datetime.now().timestamp()),
            "model": "gpt-3.5-turbo",
            "choices": [
                {
                    "index": 0,
                    "delta": {
                        "content": chunk
                    },
                    "finish_reason": None
                }
            ]
        }
        yield f"data: {json.dumps(response)}\n\n"

    # Send the final message
    yield f"data: {json.dumps({'finish_reason': 'stop'})}\n\n"


@app.post("/v1/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest):
    if request.stream:
        return StreamingResponse(
            generate_chunks(),
            media_type="text/event-stream"
        )

    # Non-streaming response (your existing code)
    response = {
        "id": f"chatcmpl-{uuid.uuid4()}",
        "object": "chat.completion",
        "created": int(datetime.datetime.now().timestamp()),
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "This is a dummy response from your custom OpenAI-compatible server."
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    }
    return response


# Image generation endpoint
@app.post("/v1/images/generations")
async def create_image(
    request: ImageGenerationRequest
):


    response = {
        "created": int(datetime.datetime.now().timestamp()),
        "data": [
            {
                "url": f"https://dummy-image-{i}.jpg",
                "b64_json": None
            }
            for i in range(request.n)
        ]
    }
    return response


# Embeddings endpoint
@app.post("/v1/embeddings")
async def create_embedding(
    request: EmbeddingRequest
):


    # Generate dummy embedding vector
    dummy_embedding = [0.1] * 1536  # OpenAI's ada-002 uses 1536 dimensions

    response = {
        "object": "list",
        "data": [
            {
                "object": "embedding",
                "embedding": dummy_embedding,
                "index": 0
            }
        ],
        "model": request.model,
        "usage": {
            "prompt_tokens": len(request.input.split()),
            "total_tokens": len(request.input.split())
        }
    }
    return response


# Moderations endpoint
@app.post("/v1/moderations")
async def create_moderation(
    request: ModerationRequest
):


    response = {
        "id": f"modr-{uuid.uuid4()}",
        "model": request.model,
        "results": [
            {
                "flagged": False,
                "categories": {
                    "sexual": False,
                    "hate": False,
                    "harassment": False,
                    "self-harm": False,
                    "sexual/minors": False,
                    "hate/threatening": False,
                    "violence/graphic": False,
                    "self-harm/intent": False,
                    "self-harm/instructions": False,
                    "harassment/threatening": False,
                    "violence": False
                },
                "category_scores": {
                    "sexual": 0.0,
                    "hate": 0.0,
                    "harassment": 0.0,
                    "self-harm": 0.0,
                    "sexual/minors": 0.0,
                    "hate/threatening": 0.0,
                    "violence/graphic": 0.0,
                    "self-harm/intent": 0.0,
                    "self-harm/instructions": 0.0,
                    "harassment/threatening": 0.0,
                    "violence": 0.0
                }
            }
        ]
    }
    return response


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}


def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    # Initialize HF client first
    init_hf_client()

    # Start the FastAPI server
    run_server()