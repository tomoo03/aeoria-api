from pydantic import BaseModel

class WhisperResponse(BaseModel):
    text: str
