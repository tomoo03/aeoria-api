from ..clients.httpxClient import HttpxClient
from ..constants.apiRequestConstant import API_REQUEST_CONSTANT
from ..dto.chatgpt import ChatGPTDto
from ..response.chatgpt import ChatGPTResponse
from typing import Any
import config

class ChatGPTApiService:
    __API_KEY: str = config.OPENAI_API_KEY
    __COMPLETION_URL: str = API_REQUEST_CONSTANT.OPENAI['COMPLETION_URL']

    def __init__(self):
        self.__httpClient = HttpxClient()

    async def create(self, dto: ChatGPTDto) -> (Any | ChatGPTResponse):
        headers = {
            API_REQUEST_CONSTANT.AUTHORIZATION: f"{API_REQUEST_CONSTANT.OPENAI['SCHEME']['AUTHORIZATION']} {self.__API_KEY}",
        }
        body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "こんにちは"}]
        }
        response: ChatGPTResponse = await self.__httpClient.json_post(self.__COMPLETION_URL, dto, headers)
        return response