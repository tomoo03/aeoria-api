import httpx
from fastapi import HTTPException, status

class HttpxClient:
    async def post(self, url: str, body, headers):
        async with httpx.AsyncClient() as client:
            response: httpx.Response = await client.post(url, data=body, headers=headers)
            print(response)
            if response.status_code != httpx.codes.OK:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            return response.json()