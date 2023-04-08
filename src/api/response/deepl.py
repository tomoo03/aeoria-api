from pydantic import BaseModel
from typing import List

class _Translations(BaseModel):
    detected_source_language: str
    text: str

class DeeplTranslateResponse(BaseModel):
    translations: List[_Translations]
