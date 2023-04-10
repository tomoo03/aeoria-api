from ..dto.chat import ChatDto
from ..response.chat import ChatResponse
from ..services.chat import ChatService
from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def get_chat_message(dto: ChatDto) -> ChatResponse:
    print("hoge")
    result = ChatService().get_chat_message(dto)
    return result