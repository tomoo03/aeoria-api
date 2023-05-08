from ..dto.chatgpt import ChatGPTMessageModel
from typing import List
from ..constants.chatGptConstant import CHAT_GPT_CONSTANT
import openai

class ChatGPTApiService:

    def chat(self, messages: List[ChatGPTMessageModel]):
        return openai.ChatCompletion.create(
            frequency_penalty=0.5,
            max_tokens=1024,
            messages=messages,
            model=CHAT_GPT_CONSTANT.MODEL['GPT_4'],
            n=1,
            presence_penalty=0.5,
            stop=None,
            stream=True,
            temperature=CHAT_GPT_CONSTANT.TEMPERATURE,
        )