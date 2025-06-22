from adk.base_step import BaseStep
from tools.classification_tool import classify_text

class ClassificationStep(BaseStep):
    def apply(self, input_data, context):
        category = classify_text(input_data)
        context["category"] = category
        return input_data, context

    def explain(self, context):
        return f"Classified the feedback as: {context.get('category', 'unknown')}"

