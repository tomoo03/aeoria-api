from ..dto.chatgpt import ChatGPTMessageModel
from typing import List
import openai

class ChatGPTApiService:

    def chat(self, messages: List[ChatGPTMessageModel]):
        return openai.ChatCompletion.create(
            frequency_penalty=0.5,
            max_tokens=1024,
            messages=messages,
            model="gpt-3.5-turbo",
            n=1,
            presence_penalty=0.5,
            stop=None,
            stream=True,
            temperature=0.5,
        )