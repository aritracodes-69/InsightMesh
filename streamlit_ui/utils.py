# Placeholder for utils.py
from agents.feedback_agent import FeedbackAgent
from agents.classification_agent import ClassificationAgent
from agents.prioritization_agent import PrioritizationAgent
from agents.action_mapper_agent import ActionMapperAgent
from agents.execution_agent import ExecutionAgent
from agents.feedback_logger_agent import FeedbackLoggerAgent
from agents.explainer_agent import ExplainerAgent


def run_feedback_pipeline(user_input):
    context = {}
    feedback_agent = FeedbackAgent()
    classification_agent = ClassificationAgent()
    prioritization_agent = PrioritizationAgent()
    action_mapper_agent = ActionMapperAgent()
    execution_agent = ExecutionAgent()
    feedback_logger_agent = FeedbackLoggerAgent()
    explainer_agent = ExplainerAgent()

    data, context = feedback_agent.run(user_input, context)
    data, context = classification_agent.run(data, context)
    data, context = prioritization_agent.run(data, context)
    data, context = action_mapper_agent.run(data, context)
    data, context = execution_agent.run(data, context)
    data, context = feedback_logger_agent.run(data, context)
    explanation, context = explainer_agent.run(data, context)

    return context