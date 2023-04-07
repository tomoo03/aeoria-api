import httpx
from fastapi import HTTPException, status
from ..dto.deepl import DeeplDto

class HttpxClient:
    async def post(self, url: str, body: DeeplDto, headers: dict[str, str]):
        async with httpx.AsyncClient() as client:
            print(url)
            print(body)
            print(headers)
            response: httpx.Response = await client.post(url, data=body, headers=headers)
            print(response.json)
            if response.status_code != httpx.codes.OK:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            json = response.json()
            return json