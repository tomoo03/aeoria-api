from ..clients.vaderSentimentClient import VaderSentimentClient

class AnalyzeService:
    def get_analyze(self, text: str):
        client = VaderSentimentClient()
        sentimentScore = client.printPolarityScores(text)
        return sentimentScore