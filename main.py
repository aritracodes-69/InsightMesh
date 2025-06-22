import os
from dotenv import load_dotenv
from datetime import datetime
import uuid

from agents.feedback_agent.builder import FeedbackAgent
from agents.classification_agent.builder import ClassificationAgent
from agents.prioritization_agent.builder import PrioritizationAgent
from agents.action_mapper_agent.builder import ActionMapperAgent
from agents.execution_agent.builder import ExecutionAgent
from agents.feedback_logger_agent.builder import FeedbackLoggerAgent
from agents.explainer_agent.builder import ExplainerAgent

from tools.bigquery_utils import ensure_table_exists, insert_feedback_record

# Load environment variables
load_dotenv()

# Ensure BigQuery table exists
ensure_table_exists()

# Instantiate agents once
feedback_agent = FeedbackAgent()
classification_agent = ClassificationAgent()
prioritization_agent = PrioritizationAgent()
action_mapper_agent = ActionMapperAgent()
execution_agent = ExecutionAgent()
feedback_logger_agent = FeedbackLoggerAgent()
explainer_agent = ExplainerAgent()


def run_full_pipeline(feedback: str):
    context = {}

    # Pipeline execution
    data, context = feedback_agent.run(feedback, context)
    data, context = classification_agent.run(data, context)
    data, context = prioritization_agent.run(data, context)
    data, context = action_mapper_agent.run(data, context)
    data, context = execution_agent.run(data, context)
    data, context = feedback_logger_agent.run(data, context)
    data, context = explainer_agent.run(data, context)

    # Record for BigQuery
    record = {
        "review_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "raw_feedback": feedback,
        "category": context.get("category"),
        "priority": context.get("priority"),
        "summary": context.get("summary"),
        "action_status": context.get("action_status"),
        "explanation": context.get("explanation"),
    }

    inserted = insert_feedback_record(record)
    context["bq_inserted"] = inserted

    return context


if __name__ == "__main__":
    print("🧠 InsightMesh Feedback Pipeline Started")
    while True:
        feedback = input("\nEnter feedback (or 'exit' to quit): ").strip()
        if feedback.lower() == "exit":
            break
        final_context = run_full_pipeline(feedback)
        print("\n📦 Final Output:")
        for key, value in final_context.items():
            print(f"  {key}: {value}")

