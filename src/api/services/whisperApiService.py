from ..clients.httpxClient import HttpxClient
from ..constants.apiRequestConstant import API_REQUEST_CONSTANT
from ..response.whisper import WhisperResponse
from fastapi import UploadFile
import config
# import openai

class WhisperApiService:
    __API_KEY: str = config.OPENAI_API_KEY
    __URLBASE: str = API_REQUEST_CONSTANT.OPENAI['URL_BASE']

    async def transcription(self, file: UploadFile) -> WhisperResponse:
        model = 'whisper-1'
        language = 'ja'
        file.file.seek(0)  # ファイルポインタを先頭に戻す
        files = {'file': (file.filename, file.file, file.content_type)}
        data = { 'file': file.filename, 'model': model, 'language': language }

        # APIリクエスト用のヘッダーを作成
        headers = {
            'Authorization': f'Bearer {self.__API_KEY}',
        }

        # APIエンドポイント
        url = f"{self.__URLBASE}/{API_REQUEST_CONSTANT.OPENAI['TRANSCRIPTION_URL']}"

        # APIリクエストを送信
        json = await HttpxClient().form_data_post(url, headers, files, data)

        return json
        # model = "whisper-1"
        # language = "ja"

        # file.file.seek(0)  # ファイルポインタを先頭に戻す
        # response = openai.Audio.transcribe(
        #     model=model,
        #     file=file.file,
        #     language=language,
        # )

        # return response