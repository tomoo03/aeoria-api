from ..clients.httpxClient import HttpxClient
from ..constants.apiConstant import API_CONSTANT
from ..dto.deepl import DeeplTranslateDto
from ..response.deepl import DeeplTranslateResponse
import config

class DeeplApiService:
    URL_BASE: str = API_CONSTANT.DEEPL['URL_BASE']

    async def translate(self, dto: DeeplTranslateDto):
        httpClient = HttpxClient()
        url: str = f"{self.URL_BASE}/{API_CONSTANT.DEEPL['TRANSLATE_PATH']}"
        headers = {
            API_CONSTANT.AUTHORIZATION: f"{API_CONSTANT.DEEPL['SCHEME']['AUTHORIZATION']} {config.DEEPL_API_KEY}",
            API_CONSTANT.CONTENT_TYPE: API_CONSTANT.DEEPL['TRANSLATE_CONTENT_TYPE']
        }
        response: DeeplTranslateResponse = await httpClient.post(url, dto, headers)
        return response