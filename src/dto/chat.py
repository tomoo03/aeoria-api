from pydantic import BaseModel
from typing import List

class ChatDto(BaseModel):
    messages: List[dict[str, str]]
    text: str