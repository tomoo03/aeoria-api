from ..clients.vaderSentimentClient import VaderSentimentClient
from ..clients.httpxClient import HttpxClient
import config

class AnalyzeService:
    async def get_analyze(self, text: str):
        url = 'https://api.deepl.com/v2/translate'
        body = { 'text': "I'm so happy.", 'target_lang': 'JA' }
        headers = { 'Authorization': f"DeepL-Auth-Key {config.DEEPL_API_KEY}", 'Content-Type': 'application/json' }
        httpClient = await HttpxClient().post(url, body, headers)
        print('httpxclient')
        print(httpClient)
        client = VaderSentimentClient()
        sentimentScore = client.printPolarityScores(text)
        return sentimentScore