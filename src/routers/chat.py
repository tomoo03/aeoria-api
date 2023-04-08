from ..dto.chat import ChatDto
from ..response.chat import ChatResponse
from ..services.chat import ChatService
from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
async def get_chat_message(dto: ChatDto) -> ChatResponse:
    print(dto)
    response = await ChatService().get_chat_message(dto)
    return response

@router.post("/chain")
def chain() -> str:
    result = ChatService().chain()
    return result