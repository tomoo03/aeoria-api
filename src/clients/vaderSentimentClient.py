from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class VaderSentimentClient:
    def __init__(self):
        self.__client = SentimentIntensityAnalyzer()

    def printPolarityScores(self, text: str):
        sentimentScore = self.__client.polarity_scores(text)
        print(sentimentScore)
        return sentimentScore