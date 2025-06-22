#test_classification.py
from agents.classification_agent.steps.classification_step import ClassificationStep

def test_classification_agent():
    agent = ClassificationStep()
    result, context = agent.run("great ui experience", {})
    assert "category" in context
