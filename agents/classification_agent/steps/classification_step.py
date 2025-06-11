# Placeholder for classification_step.py
from adk.base_step import BaseStep
class ClassificationStep(BaseStep):
 def apply(self, input_data, context):
    if "error" in input_data.lower():
        category = "bug_report"
    elif "feature" in input_data.lower():
        category = "feature_request"
    else:
        category = "general"
    context['category'] = category
    return category, context
 def explain(self):
    return "Classified feedback category."
