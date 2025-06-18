# Placeholder for test_feedback.py
from agents.feedback_agent import FeedbackAgent

def test_feedback_agent():
    agent = FeedbackAgent()
    result, context = agent.run("Great UI", {})
    assert isinstance(result, str)
    assert "feedback_text" in context
