from ..dto.chat import ChatDto
from ..response.chat import ChatResponse
from ..services.chat import ChatService
from fastapi import APIRouter, Response
import asyncio
router = APIRouter()

@router.post("/chat")
async def get_chat_message(dto: ChatDto):
    print("hoge")
    result = ChatService().get_chat_message(dto)
    print("fuga")
    async def event_stream():
        counter = 0
        while counter < 10:
            counter += 1
            await asyncio.sleep(1)
            yield result
    return Response(event_stream(), media_type="text/event-stream")