from ..api.response.whisper import WhisperResponse
from ..api.services.whisperApiService import WhisperApiService

class TranscriptionsService:
    def __init__(self):
        self.__whisperApi = WhisperApiService()

    def get_transcriptions(self, file: bytes) -> WhisperResponse:
        return self.__whisperApi.transcription(file)