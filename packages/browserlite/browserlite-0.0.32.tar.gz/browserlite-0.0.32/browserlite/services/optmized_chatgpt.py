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

    def process_response(self, response: str) -> str:
        text_v1 = response.strip()
        match = re.search(r'ChatGPT says: (.*)', text_v1)
        if match:
            result = match.group(1)
        else:
            result = ""
        return result

    def perform_search(self, query: str,sleep=None) -> str:
        formatted_query = self.format_query(query)
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
