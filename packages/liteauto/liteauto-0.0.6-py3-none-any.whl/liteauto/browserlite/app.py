from typing import Literal

from .core.automation import AutomationManager, SearchServiceType

BrowserType = Literal[
    'google-chrome',
    'microsoft-edge-stable',
    'firefox'
]


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


def chatgpt(query, sleep=None, web_search=False,
            each_chat_start_wait_time=0,
            batch_wait_size=4,
            batch_wait_time=10
            ):
    return browse(
        query,
        service_name="chatgpt",
        base_url="http://www.chatgpt.com/",
        sleep=sleep,
        web_search=web_search,
        each_chat_start_wait_time=each_chat_start_wait_time,
        batch_wait_size=batch_wait_size,
        batch_wait_time=batch_wait_time
    )


def huggingchat(query, sleep=None, web_search=False,
                each_chat_start_wait_time=0,
                batch_wait_size=4,
                batch_wait_time=10
                ):
    return browse(
        query,
        service_name="huggingchat",
        base_url="https://huggingface.co/chat/",
        sleep=sleep,
        web_search=web_search,
        each_chat_start_wait_time=each_chat_start_wait_time,
        batch_wait_size=batch_wait_size,
        batch_wait_time=batch_wait_time
    )
