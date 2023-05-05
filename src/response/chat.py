from ..api.dto.chatgpt import ChatGPTMessageModel
from pydantic import BaseModel
from typing import Any, Generator, List

class ChatResponse(BaseModel):
    status: str
    message_category: str
    messages: List[ChatGPTMessageModel] | None
    message: str | None

class ChatResponseGenerator:
    def __init__(self, generator: Generator[Any | list | dict, None, None], messages: List[ChatGPTMessageModel]):
        self.generator: Generator[Any | list | dict, None, None] = generator
        self.messages: List[ChatGPTMessageModel] = messages

    def to_dict(self):
        return vars(self)