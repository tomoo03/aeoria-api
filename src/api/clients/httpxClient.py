from ..dto.deepl import DeeplDto
from ..dto.chatgpt import ChatGPTDto
from fastapi import HTTPException, status
from typing import Any, BinaryIO
import httpx

class HttpxClient:
    def __init__(self):
        self.__httpx = httpx

    async def form_post(self, url: str, data: Any, headers: dict[str, str]) -> Any:
        async with self.__httpx.AsyncClient() as client:
            print(url)
            print(data)
            print(headers)
            response: httpx.Response = await client.post(url, data=data, headers=headers, timeout=180.0)
            print(response)
            if response.status_code != httpx.codes.OK:
                print(response)
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            json = response.json()
            return json

    async def json_post(self, url: str, body: ChatGPTDto, headers: dict[str, str]) -> Any:
        async with self.__httpx.AsyncClient() as client:
            print(url)
            print(body)
            print(headers)
            response: httpx.Response = await client.post(url, json=body, headers=headers, timeout=180.0)
            print(response)
            if response.status_code != httpx.codes.OK:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            json = response.json()
            return json

    async def form_data_post(self, url: str, headers: dict[str, str], files: dict[str, tuple[str | None, BinaryIO, str | None]], data: Any):
        async with self.__httpx.AsyncClient() as client:
            print(url)
            print(headers)
            print(files)
            print(data)
            response: httpx.Response = await client.post(url, headers=headers, files=files, data=data, timeout=180.0)
            if response.status_code != httpx.codes.OK:
                print(response)
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            json = response.json()
            return json