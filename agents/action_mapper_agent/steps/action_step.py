# Placeholder for action_step.py
from adk.base_step import BaseStep

class ActionStep(BaseStep):
    def apply(self, input_data, context):
        mapping = {
            "bug_report": "create_ticket",
            "feature_request": "notify_team",
            "general": "archive"
        }
        action = mapping.get(context.get('category'), "archive")
        context['action'] = action
        return action, context

    def explain(self):
        return "Mapped category to action."
