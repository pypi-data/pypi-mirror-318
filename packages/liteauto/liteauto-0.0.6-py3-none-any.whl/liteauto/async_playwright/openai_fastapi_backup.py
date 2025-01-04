import asyncio
import json
import uuid
import datetime
from contextlib import asynccontextmanager
from typing import Optional, Dict, Any, List, Union, AsyncGenerator

import uvicorn
from fastapi import FastAPI, HTTPException, Header, Request, WebSocket
from pydantic import BaseModel, Field

from liteauto.async_playwright._oai import ChatHFClient
from fastapi.responses import StreamingResponse


hf_client:Union[ChatHFClient,None] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global hf_client
    hf_client = await ChatHFClient.create(headless=True)
    yield
    # Shutdown
    if hf_client:
        await hf_client.close()

app = FastAPI(title="OpenAI Compatible API", lifespan=lifespan)


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


async def generate_chunks(messages: List[Dict[str, str]]) -> AsyncGenerator[str, None]:
    """Async generator for streaming responses"""
    completion = await hf_client.completions.create(
        messages=messages,
        stream=True,
        web_search=False
    )

    async for chunk in completion:
        response = {
            "id": f"chatcmpl-{uuid.uuid4()}",
            "object": "chat.completion.chunk",
            "created": int(datetime.datetime.now().timestamp()),
            "model": "gpt-3.5-turbo",
            "choices": [
                {
                    "index": 0,
                    "delta": {
                        "content": chunk.choices[0].delta.content
                    },
                    "finish_reason": None
                }
            ]
        }
        yield f"data: {json.dumps(response)}\n\n"

    # Send final message
    yield f"data: {json.dumps({'finish_reason': 'stop'})}\n\n"


@app.post("/v1/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest):
    if request.stream:
        return StreamingResponse(
            generate_chunks([{"role": m.role, "content": m.content} for m in request.messages]),
            media_type="text/event-stream"
        )

    # Non-streaming response
    response = await hf_client.completions.create(
        messages=[{"role": m.role, "content": m.content} for m in request.messages],
        stream=False,
        web_search=False
    )

    return {
        "id": f"chatcmpl-{uuid.uuid4()}",
        "object": "chat.completion",
        "created": int(datetime.datetime.now().timestamp()),
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")