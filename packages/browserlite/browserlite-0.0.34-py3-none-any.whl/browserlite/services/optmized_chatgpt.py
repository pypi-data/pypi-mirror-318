import re
import time

import pyautogui

from .base import SearchService
from ..core.autoclip import AutoClip
from ..config import AutomationConfig
from ..core.autoweb import AutoWeb


class OPTChatGPTSearch(SearchService):
    """ChatGPT search implementation"""

    def format_query(self, query: str) -> str:
        return f"{query}"

    def process_response(self, response: str,**kwargs) -> str:
        text_v1 = response.strip()
        match = re.search(r'ChatGPT says: (.*)', text_v1)
        if match:
            result = match.group(1)
        else:
            result = ""
        return result

    def perform_search(self, query: str,sleep=None,web_search: bool = False) -> str:
        formatted_query = self.format_query(query)
        if web_search:
            query += ', Use websearch Tool'
        try:
            w, h = pyautogui.size()
            pyautogui.click(w - w/2, h - 60)
            time.sleep(2)
            AutoWeb.search(formatted_query)
            start_time = time.time()
            pyautogui.click(w - 50, h - 100)
            max_time = sleep or AutomationConfig.delays.chatgpt_text_process_time

            answer = ""
            previous = ""
            while True:
                time.sleep(AutomationConfig.delays.chatgpt_text_process_time)
                text = AutoClip.get_clipboard_content()
                if text == previous or (time.time() - start_time > max_time):
                    answer = text
                    break
                previous = text
            return self.process_response(answer)


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
            if batch_wait_size and i % batch_wait_size == 0:
                time.sleep(batch_wait_time)
            pyautogui.click(227, 132) #New chat button position
            time.sleep(1)
            result = self.perform_search(q)
            results.append(result)

        return results
