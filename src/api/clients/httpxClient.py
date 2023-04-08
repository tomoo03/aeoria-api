from ..dto.deepl import DeeplDto
from ..dto.chatgpt import ChatGPTDto
from fastapi import HTTPException, status
from typing import Any
import httpx

class HttpxClient:
    def __init__(self):
        self.__httpx = httpx

    async def form_post(self, url: str, data: DeeplDto, headers: dict[str, str]) -> Any:
        async with self.__httpx.AsyncClient() as client:
            print(url)
            print(data)
            print(headers)
            response: httpx.Response = await client.post(url, data=data, headers=headers, timeout=60.0)
            print(response)
            print(response.status_code)
            if response.status_code != httpx.codes.OK:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            json = response.json()
            return json

    async def json_post(self, url: str, body: ChatGPTDto, headers: dict[str, str]) -> Any:
        async with self.__httpx.AsyncClient() as client:
            print(url)
            print(body)
            print(headers)
            response: httpx.Response = await client.post(url, json=body, headers=headers, timeout=60.0)
            print(response)
            print(response.status_code)
            if response.status_code != httpx.codes.OK:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            json = response.json()
            return json