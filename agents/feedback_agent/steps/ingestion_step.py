from adk.base_step import BaseStep
from tools.feedback_tool import preprocess_feedback

class IngestionStep(BaseStep):
    def apply(self, input_data, context):
        cleaned = preprocess_feedback(input_data)
        context["cleaned_feedback"] = cleaned
        return cleaned, context

    def explain(self):
        return "Ingested and preprocessed the feedback."
