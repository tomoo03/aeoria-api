from pydantic import BaseModel
from typing import TypeVar

class DeeplTranslateDto(BaseModel):
    source_lang: str
    text:  str
    target_lang: str

DeeplDto = TypeVar("DeeplDto", DeeplTranslateDto, any)