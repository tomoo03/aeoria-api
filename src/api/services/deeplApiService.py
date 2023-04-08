from ..clients.httpxClient import HttpxClient
from ..constants.apiRequestConstant import API_REQUEST_CONSTANT
from ..dto.deepl import DeeplTranslateDto
from ..response.deepl import DeeplTranslateResponse
import config

class DeeplApiService:
    __API_KEY: str = config.DEEPL_API_KEY
    __URL_BASE: str = API_REQUEST_CONSTANT.DEEPL['URL_BASE']

    def __init__(self):
        self._httpClient = HttpxClient()

    async def translate(self, dto: DeeplTranslateDto) -> DeeplTranslateResponse:
        url: str = f"{self.__URL_BASE}/{API_REQUEST_CONSTANT.DEEPL['TRANSLATE_PATH']}"
        headers = {
            API_REQUEST_CONSTANT.AUTHORIZATION: f"{API_REQUEST_CONSTANT.DEEPL['SCHEME']['AUTHORIZATION']} {self.__API_KEY}",
        }
        response: DeeplTranslateResponse = await self._httpClient.form_post(url, dto, headers)
        return response