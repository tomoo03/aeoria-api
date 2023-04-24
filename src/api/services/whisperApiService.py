from ..response.whisper import WhisperResponse
import openai

class WhisperApiService:
    def transcription(self, file: bytes) -> WhisperResponse:
        model = "whisper-1"
        language = "ja"
        return openai.Audio.transcribe(
            model=model,
            file=file,
            language=language
        )