# agents/feedback_agent.py

from adk.base_agent import BaseAgent
from agents.feedback_steps.ingestion_step import IngestionStep
from agents.feedback_steps.sentiment_step import SentimentStep

class FeedbackAgent(BaseAgent):
    def __init__(self):
        self.steps = [
            IngestionStep(),
            SentimentStep()
        ]

    def run(self, input_data, context):
        for step in self.steps:
            input_data, context = step.apply(input_data, context)
        return input_data, context
