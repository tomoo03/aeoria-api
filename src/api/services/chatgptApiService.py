from ..clients.httpxClient import HttpxClient
from ..constants.apiRequestConstant import API_REQUEST_CONSTANT
from ..constants.chatGptConstant import CHAT_GPT_CONSTANT
from ..dto.chatgpt import ChatGPTMessageModel
from typing import List
import config
import openai

class ChatGPTApiService:
    __API_KEY: str = config.OPENAI_API_KEY
    __COMPLETION_URL: str = API_REQUEST_CONSTANT.OPENAI['COMPLETION_URL']

    def __init__(self):
        self.__httpClient = HttpxClient()

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