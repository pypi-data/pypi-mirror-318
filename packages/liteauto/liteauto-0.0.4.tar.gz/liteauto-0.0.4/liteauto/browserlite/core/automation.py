from typing import Dict, Optional, Literal
import pyautogui
from ..services import HuggingChatSearch,GoogleSearch,OPTChatGPTSearch
from ..core.autoweb import AutoWeb

SearchServiceType = Literal["openai","google","huggingchat","chatgpt"]

_SERVICE_NAME_MAP = {
    "chatgptsearch":"chatgpt",
    "chatgpt":"chatgpt",
    "openai":"chatgpt",
    "huggingchat":"huggingchat"
}

class AutomationManager:
    """Main automation manager class"""

    def __init__(self):
        pyautogui.FAILSAFE = True
        self.services: Dict= {
            "chatgpt": OPTChatGPTSearch(),
            "huggingchat": HuggingChatSearch(),
            "google":GoogleSearch()
        }

    def execute_search(self, query: str, service_name: SearchServiceType="google",
                       browser="microsoft-edge-stable",
                       base_url:str|None = None,
                       sleep:int|None=None,
                       web_search=False,
                       **kwargs) -> Optional[str]:
        """Execute a search using the specified service"""
        name = _SERVICE_NAME_MAP.get(service_name, "google")

        # if service_name=="chatgpt":
        #     query = f"https://www.{name}.com/search?q={query}"

        service:HuggingChatSearch|OPTChatGPTSearch = self.services.get(name)

        if not service:
            print(f"Service {service_name} not found")
            return None

        if not AutoWeb.open(base_url=base_url,
                            browser_name=browser):
            return None

        try:
            if isinstance(query,list):
                result = service.multi_search(query,
                                              each_chat_start_wait_time=kwargs.get("each_chat_start_wait_time", 0),
                                              batch_wait_size=kwargs.get("batch_wait_size", 4),
                                              batch_wait_time=kwargs.get("batch_wait_time", 10))
            else:
                result = service.perform_search(query=query,
                                            sleep=sleep,
                                            web_search=web_search)
            return result
        finally:
            AutoWeb.close()

