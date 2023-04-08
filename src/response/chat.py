from ..api.dto.chatgpt import ChatGPTMessageModel
from pydantic import BaseModel
from typing import List

class ChatResponse(BaseModel):
    messages: List[ChatGPTMessageModel]
