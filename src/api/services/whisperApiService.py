from ..response.whisper import WhisperResponse
from fastapi import UploadFile
import openai

class WhisperApiService:
    def transcription(self, file: UploadFile) -> WhisperResponse:
        model = "whisper-1"
        language = "ja"

        file.file.seek(0)  # ファイルポインタを先頭に戻す
        response = openai.Audio.transcribe(
            model=model,
            file=file.file,
            language=language,
        )

        return response