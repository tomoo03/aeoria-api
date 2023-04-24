from ..api.response.whisper import WhisperResponse
from ..services.transcriptions import TranscriptionsService
from fastapi import APIRouter, Depends, File, UploadFile

router = APIRouter()

# ボイスチャットAPI
@router.post("/voice-chat")
async def voice_chat(
    file: UploadFile = File(...),
    transcriptionsService: TranscriptionsService = Depends(TranscriptionsService)
) -> WhisperResponse:
    contents = await file.read()
    return transcriptionsService.get_transcriptions(contents)