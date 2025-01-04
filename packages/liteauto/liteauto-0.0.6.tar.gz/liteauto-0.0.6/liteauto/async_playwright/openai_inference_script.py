from __future__ import annotations

import os
import json
import httpx
import asyncio
from typing import Dict, List, Optional, Union, AsyncIterator, Any, Mapping
from typing_extensions import Literal
from pydantic import BaseModel
import datetime
import uuid
from dataclasses import dataclass
from functools import cached_property


# Exception Classes
class APIError(Exception):
    def __init__(
        self,
        message: str,
        code: int | None = None,
        response: httpx.Response | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.response = response


class TimeoutError(APIError):
    pass


class APIConnectionError(APIError):
    pass


class APIStatusError(APIError):
    pass


# Base Models remain the same
class ChatCompletionMessage(BaseModel):
    role: str
    content: str


class CompletionUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class Choice(BaseModel):
    finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
    index: int
    message: ChatCompletionMessage


class ChatCompletion(BaseModel):
    id: str
    choices: List[Choice]
    created: int
    model: str
    object: Literal["chat.completion"]
    usage: Optional[CompletionUsage] = None


class ChatCompletionStreamChoice(BaseModel):
    delta: Dict[str, Any]
    index: int
    finish_reason: Optional[str] = None


class ChatCompletionChunk(BaseModel):
    id: str
    choices: List[ChatCompletionStreamChoice]
    created: int
    model: str
    object: Literal["chat.completion.chunk"]


# Timeout configuration
class Timeout:
    def __init__(
        self,
        connect: float | None = None,
        read: float | None = None,
        write: float | None = None,
        pool: float | None = None,
    ):
        self.connect = connect
        self.read = read
        self.write = write
        self.pool = pool

    def as_dict(self) -> dict:
        return {
            "connect": self.connect,
            "read": self.read,
            "write": self.write,
            "pool": self.pool
        }


# Base Client Classes
class APIResource:
    def __init__(self, client: Union[OpenAI, AsyncOpenAI]) -> None:
        self._client = client

    def _make_status_error(self, response: httpx.Response) -> APIStatusError:
        if response.status_code == 408 or response.status_code == 504:
            return TimeoutError(
                message=f"Request timed out: {response.text}",
                code=response.status_code,
                response=response
            )
        return APIStatusError(
            message=f"Request failed with status code {response.status_code}: {response.text}",
            code=response.status_code,
            response=response
        )


class SyncAPIResource(APIResource):
    pass


class AsyncAPIResource(APIResource):
    pass


# Completions Implementation
class Completions(SyncAPIResource):
    def create(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float = 1.0,
        stream: bool = False,
        **kwargs
    ) -> Union[ChatCompletion, AsyncIterator[ChatCompletionChunk]]:
        url = f"{self._client.base_url}/v1/chat/completions"

        payload = {
            "messages": messages,
            "model": model,
            "temperature": temperature,
            "stream": stream,
            **kwargs
        }

        timeout = httpx.Timeout(
            connect=self._client.timeout.connect,
            read=self._client.timeout.read,
            write=self._client.timeout.write,
            pool=self._client.timeout.pool
        )

        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.post(url, json=payload)

                if response.status_code != 200:
                    raise self._make_status_error(response)

                return ChatCompletion(**response.json())
        except httpx.TimeoutException as e:
            raise TimeoutError(
                message="Request timed out. Please try again.",
                code=None
            ) from e
        except httpx.NetworkError as e:
            raise APIConnectionError(
                message="Network error occurred. Please check your connection.",
                code=None
            ) from e


class AsyncCompletions(AsyncAPIResource):
    def create(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float = 1.0,
        stream: bool = False,
        **kwargs
    ) -> Union[ChatCompletion, AsyncIterator[ChatCompletionChunk]]:
        async def _create():
            url = f"{self._client.base_url}/v1/chat/completions"

            payload = {
                "messages": messages,
                "model": model,
                "temperature": temperature,
                "stream": stream,
                **kwargs
            }

            timeout = httpx.Timeout(
                connect=self._client.timeout.connect,
                read=self._client.timeout.read,
                write=self._client.timeout.write,
                pool=self._client.timeout.pool
            )

            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.post(url, json=payload)

                    if response.status_code != 200:
                        raise self._make_status_error(response)

                    return ChatCompletion(**response.json())
            except httpx.TimeoutException as e:
                raise TimeoutError(
                    message="Request timed out. Please try again.",
                    code=None
                ) from e
            except httpx.NetworkError as e:
                raise APIConnectionError(
                    message="Network error occurred. Please check your connection.",
                    code=None
                ) from e

        try:
            loop = asyncio.get_running_loop()
            return loop.create_task(_create())
        except RuntimeError:
            return asyncio.run(_create())


# Chat Implementation remains the same
class Chat(SyncAPIResource):
    @cached_property
    def completions(self) -> Completions:
        return Completions(self._client)


class AsyncChat(AsyncAPIResource):
    @cached_property
    def completions(self) -> AsyncCompletions:
        return AsyncCompletions(self._client)


# Main Client Classes
class OpenAI:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "http://localhost:8000",
        timeout: Optional[Union[float, Timeout]] = None
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url

        # Configure timeout
        if timeout is None:
            self.timeout = Timeout(connect=10.0, read=30.0, write=30.0, pool=5.0)
        elif isinstance(timeout, (int, float)):
            self.timeout = Timeout(connect=timeout, read=timeout, write=timeout, pool=timeout)
        else:
            self.timeout = timeout

        self.chat = Chat(self)


class AsyncOpenAI:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "http://localhost:8000",
        timeout: Optional[Union[float, Timeout]] = None
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url

        # Configure timeout
        if timeout is None:
            self.timeout = Timeout(connect=10.0, read=30.0, write=30.0, pool=5.0)
        elif isinstance(timeout, (int, float)):
            self.timeout = Timeout(connect=timeout, read=timeout, write=timeout, pool=timeout)
        else:
            self.timeout = timeout

        self.chat = AsyncChat(self)


# Client Aliases for compatibility
Client = OpenAI
AsyncClient = AsyncOpenAI


# # Sync client
# client = OpenAI()
#
# # Simple usage without await
# response = client.chat.completions.create(
#     messages=[{"role": "user", "content": "1+2=? just answer"}],
#     model="your-model-name"
# )
# print(response.choices[0].message.content)

# Async client
async_client = AsyncOpenAI()

# Also no await needed for the create() call
response = async_client.chat.completions.create(
    messages=[{"role": "user", "content": "Hello!"}],
    model="your-model-name"
)
print(response.choices[0].message.content)