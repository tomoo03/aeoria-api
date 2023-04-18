from ..api.dto.chatgpt import ChatGPTMessageModel
from pydantic import BaseModel
from typing import Any, Generator, List

class ChatResponse(BaseModel):
    messages: List[ChatGPTMessageModel]

class ChatResponseGenerator:
    def __init__(self, generator: Generator[Any | list | dict, None, None], messages: List[ChatGPTMessageModel]):
        self.generator: Generator[Any | list | dict, None, None] = generator
        self.messages: List[ChatGPTMessageModel] = messages
