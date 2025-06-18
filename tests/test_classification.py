# Placeholder for test_classification.py
from agents.classification_agent import ClassificationAgent

def test_classification_agent():
    agent = ClassificationAgent()
    result, context = agent.run("great ui experience", {})
    assert "category" in context
