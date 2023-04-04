from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class VaderSentimentClient:
    def __init__(self):
        self.__client = SentimentIntensityAnalyzer()

    def printPolarityScores(self, text: str):
        vs = self.__client.polarity_scores(text)
        print(vs)
        return vs