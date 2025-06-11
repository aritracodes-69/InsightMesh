# Placeholder for sentiment_step.py
from adk.base_step import BaseStep
class SentimentStep(BaseStep):
    def apply(self, input_data, context):
        sentiment = "positive" if "good" in input_data.lower() else "negative"
        context['sentiment'] = sentiment
        return sentiment, context
    def explain(self):
        return "Performed sentiment analysis on feedback."