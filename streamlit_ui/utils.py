from agents.feedback_agent.builder import FeedbackAgent
from agents.classification_agent.steps.classification_step import ClassificationStep
from agents.prioritization_agent.steps.priority_step import PriorityStep
from agents.action_mapper_agent.steps.action_step import ActionStep
from agents.execution_agent.steps.execute_step import ExecuteStep
from agents.feedback_logger_agent.steps.logger_step import LoggerStep
from agents.explainer_agent.steps.explainer_step import ExplainerStep
from agents.summarizer_agent.steps.summarizer_step import SummarizationStep
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def run_feedback_pipeline(user_input: str):
    """
    Runs the full InsightMesh multi-agent pipeline.

    Args:
        user_input (str): Raw user feedback input.

    Returns:
        context (dict): Dictionary holding agent outputs and shared state.
        explanation (str): Human-readable explanation of classification and prioritization.
    """
    context = {}

    # Initialize agents
    feedback_agent = FeedbackAgent()  # Full agent, not just a single step
    classification_agent = ClassificationStep()
    prioritization_agent = PriorityStep()
    action_mapper_agent = ActionStep()
    execution_agent = ExecuteStep()
    feedback_logger_agent = LoggerStep()
    explainer_agent = ExplainerStep()
    summarizer_agent = SummarizationStep()

    # Execute agent chain
    data, context = feedback_agent.run(user_input, context)
    data, context = classification_agent.apply(data, context)
    data, context = prioritization_agent.apply(data, context)
    data, context = action_mapper_agent.apply(data, context)
    data, context = execution_agent.apply(data, context)
    data, context = feedback_logger_agent.apply(data, context)

    explanation, context = explainer_agent.apply(data, context)
    summary, context = summarizer_agent.apply(data, context)

    context["summary"] = summary
    context["explanation"] = explanation

    return context, explanation


