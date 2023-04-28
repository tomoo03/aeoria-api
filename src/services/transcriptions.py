from ..api.response.whisper import WhisperResponse
from ..api.services.whisperApiService import WhisperApiService
from fastapi import UploadFile

class TranscriptionsService:
    def __init__(self):
        self.__whisperApi = WhisperApiService()

    async def get_transcriptions(self, file: UploadFile) -> WhisperResponse:
        contents = await self.__whisperApi.transcription(file)
        print(contents)
        return contents