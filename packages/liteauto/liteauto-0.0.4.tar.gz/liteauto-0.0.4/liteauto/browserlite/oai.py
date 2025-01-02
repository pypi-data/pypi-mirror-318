import asyncio
from random import choices
from typing import Literal, List, Dict, Optional, Union, TypedDict
from dataclasses import dataclass

SearchServiceType = Literal["huggingchat", "chatgpt"]
BrowserType = Literal['google-chrome', 'microsoft-edge-stable', 'firefox']


def browse(
    query,
    service_name: SearchServiceType = "google",
    browser: BrowserType = 'microsoft-edge-stable',
    base_url="http://www.google.com/",
    sleep: int | None = None,
    web_search=False,
    **kwargs):
    manager = AutomationManager()
    result = manager.execute_search(
        query=query,
        service_name=service_name,
        browser=browser,
        base_url=base_url,
        sleep=sleep,
        web_search=web_search,
        **kwargs
    )
    return result






class AIBrowserClient:
    """
    Client for browser-based chat models.
    """

    def __init__(
        self,
        browser: BrowserType = 'microsoft-edge-stable',
        default_sleep: Optional[int] = 30,
        default_batch_settings: Optional[Dict] = None
    ):
        self.browser = browser
        self.default_sleep = default_sleep
        self.default_batch_settings = default_batch_settings or {
            "each_chat_start_wait_time": 0,
            "batch_wait_size": 4,
            "batch_wait_time": 10
        }
        self.chat = ChatCompletion(self)

def is_list_of_lists(var):
    return isinstance(var, list) and all(isinstance(item, list) for item in var)


from typing import Literal, List, Dict, Optional, Union, TypedDict, Iterator, Generator
from dataclasses import dataclass
import time

from browserlite.core.automation import AutomationManager

SearchServiceType = Literal["huggingchat", "chatgpt"]
BrowserType = Literal['google-chrome', 'microsoft-edge-stable', 'firefox']


@dataclass
class DeltaMessage:
    role: Optional[str] = None
    content: Optional[str] = None


@dataclass
class StreamChoice:
    delta: DeltaMessage
    finish_reason: Optional[str] = None
    index: int = 0


@dataclass
class ChatCompletionChunk:
    id: str
    choices: List[StreamChoice]
    created: int
    model: str
    object: str = "chat.completion.chunk"


@dataclass
class Conversation:
    role: Literal["system", "user", "assistant"]
    content: str

@dataclass
class Message:
    message:Conversation


@dataclass
class ChatCompletionResponse:
    choices: List[Message]
    model: str
    usage: Dict[str, int]


def chunk_string(text: str, chunk_size: int = 4) -> Iterator[str]:
    """Split text into chunks of specified size."""
    return (text[i:i + chunk_size] for i in range(0, len(text), chunk_size))


class ChatCompletion:
    """
    Handles chat completion operations for the BrowserChat client.
    """

    def __init__(self, client: 'AIBrowserClient'):
        self.client = client
        self._service_configs = {
            "huggingchat": {
                "base_url": "https://huggingface.co/chat/",
                "service_name": "huggingchat"
            },
            "chatgpt": {
                "base_url": "http://www.chatgpt.com/",
                "service_name": "chatgpt"
            }
        }

    def create(
        self,
        messages: List[Dict] | List[List[Dict]] | str | List[str],
        model: SearchServiceType = "chatgpt",
        temperature: float = 1.0,
        max_tokens: Optional[int] = None,
        sleep: Optional[int] = None,
        batch_settings: Dict = None,
        stream: bool = False,
        **kwargs
    ) -> Union[ChatCompletionResponse, Generator[ChatCompletionChunk, None, None],List[str],str]:
        """
        Create a chat completion using browser-based LLMs.

        Args:
            messages: List of message objects with role and content
            model: The model to use (huggingchat or chatgpt)
            temperature: Controls randomness (not implemented in browser version)
            max_tokens: Maximum tokens to generate (not implemented in browser version)
            sleep: Optional sleep time between requests
            web_search: Whether to enable web search
            batch_settings: Dictionary containing batch-related settings
            stream: Whether to stream the response
        """
        sleep = sleep if sleep is not None else self.client.default_sleep
        batch_settings = {**self.client.default_batch_settings, **(batch_settings or {})}
        service_config = self._service_configs[model]

        if isinstance(messages, str):
            prompt = messages
        elif isinstance(messages, list) and isinstance(messages[0], str):
            prompt = messages
        elif is_list_of_lists(messages):
            prompt = [self._format_messages(message) for message in messages]
        else:
            prompt = self._format_messages(messages)

        response = browse(
            query=prompt,
            service_name=service_config["service_name"],
            browser=self.client.browser,
            base_url=service_config["base_url"],
            sleep=sleep,
            web_search=kwargs.get("web_search",False),
            each_chat_start_wait_time=batch_settings["each_chat_start_wait_time"],
            batch_wait_size=batch_settings["batch_wait_size"],
            batch_wait_time=batch_settings["batch_wait_time"]
        )

        if stream:
            return self._stream_response(response, model)

        if isinstance(response, list):
            choices = [Message(
                message=Conversation(
                    role='assistant',
                    content=r
                )
            )for r in response]
        else:
            choices = [Message(
                message=Conversation(
                    role='assistant',
                    content=response
                )
            )]
        if kwargs.get('return_type',"")=='str':
            return choices[0].message.content if len(choices)==1 else [c.message.content for c in choices]
        return ChatCompletionResponse(
            choices=choices,
            model=model,
            usage={"total_tokens": -1}
        )

    def _stream_response(
        self,
        response: Union[str, List[str]],
        model: str
    ) -> Generator[ChatCompletionChunk, None, None]:
        """Stream the response in chunks."""
        if isinstance(response, list):
            for idx, resp in enumerate(response):
                yield from self._stream_single_response(resp, model, idx)
        else:
            yield from self._stream_single_response(response, model, 0)

    def _stream_single_response(
        self,
        text: str,
        model: str,
        response_index: int
    ) -> Generator[ChatCompletionChunk, None, None]:
        """Stream a single response text."""
        created_time = int(time.time())

        # First chunk with role
        yield ChatCompletionChunk(
            id=f"chat-{created_time}",
            choices=[StreamChoice(
                delta=DeltaMessage(role="assistant"),
                index=response_index
            )],
            created=created_time,
            model=model
        )

        # Content chunks
        for chunk in chunk_string(text):
            yield ChatCompletionChunk(
                id=f"chat-{created_time}",
                choices=[StreamChoice(
                    delta=DeltaMessage(content=chunk),
                    index=response_index
                )],
                created=created_time,
                model=model
            )

        # Final chunk with finish reason
        yield ChatCompletionChunk(
            id=f"chat-{created_time}",
            choices=[StreamChoice(
                delta=DeltaMessage(),
                finish_reason="stop",
                index=response_index
            )],
            created=created_time,
            model=model
        )

    def _format_messages(self, messages: List[Dict] | str) -> str:
        """Format message list into a single prompt string."""
        formatted = []
        for msg in messages:
            if msg.get('role') == "system":
                formatted.append(f"System: {msg['content']}")
            elif msg.get('role') == "user":
                formatted.append(f"Human: {msg['content']}")
            elif msg.get('role') == "assistant":
                formatted.append(f"Assistant: {msg['content']}")
        return "\n".join(formatted)

