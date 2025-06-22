from adk.base_step import BaseStep
from textblob import TextBlob

class SentimentStep(BaseStep):
    def apply(self, input_data, context):
        blob = TextBlob(input_data)
        polarity = blob.sentiment.polarity
        sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
        context["sentiment"] = sentiment
        return input_data, context

    def explain(self,context):
        return f"Detected sentiment as: {context.get('sentiment', 'unknown')}."


