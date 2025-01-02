import re
import time
import pyautogui
from .base import SearchService
from ..core.autoclip import AutoClip
from ..config import AutomationConfig
from ..core.autoweb import AutoWeb


class HuggingChatSearch(SearchService):
    """ChatGPT search implementation"""

    def format_query(self, query: str) -> str:
        return "".join(query.splitlines()) + "[ANS]"

    def process_response(self, response: str,**kwargs) -> str:
        try:
            match = re.search(r'\[ANS\](.*)Ask anything',response,re.DOTALL)
            if match:
                response = match.group(1).strip()
            else:
                match = re.search(r'\[ANS\](.*)', response, re.DOTALL)
                if match:
                    response = match.group(1).strip()
        except Exception as e:
            print(f"Error parsing response: {e}")
            return ""
        return response

    def perform_search(self, query: str, sleep=None, web_search: bool = False) -> str:
        query = self.format_query(query)
        try:
            w, h = pyautogui.size()
            if web_search:
                time.sleep(1)
                pyautogui.click(416, 685)  # 582 diff: 103
                time.sleep(1)
                pyautogui.click(416, 645)

            pyautogui.click(416, 645)
            time.sleep(1)
            AutoWeb.search(query)
            start_time = time.time()
            pyautogui.click(w - 20, h - 20)
            max_time = sleep or AutomationConfig.delays.chatgpt_text_process_time
            if web_search:
                time.sleep(10)

            prev = ""
            while True:
                time.sleep(AutomationConfig.delays.chatgpt_text_process_time)
                text = AutoClip.get_clipboard_content()
                if text == prev or (time.time() - start_time > max_time):
                    return self.process_response(response=text)
                prev = text


        except Exception as e:
            print(f"Error performing search: {e}")
            return ""

    def multi_search(self, queries: list,
                     each_chat_start_wait_time=0,
                     batch_wait_size=4,
                     batch_wait_time=10):
        results = []
        for i, q in enumerate(queries, 1):
            time.sleep(each_chat_start_wait_time)
            if batch_wait_size and i % batch_wait_size == 0 and i!=0:
                time.sleep(batch_wait_time)
            pyautogui.click(244, 132) #New chat button position
            time.sleep(1)
            result = self.perform_search(q)
            results.append(result)

        return results
