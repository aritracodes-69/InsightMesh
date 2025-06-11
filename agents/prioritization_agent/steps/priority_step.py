# Placeholder for priority_step.py
from adk.base_step import BaseStep

class PriorityStep(BaseStep):
    def apply(self, input_data, context):
        priority = "high" if context.get('category') == "bug_report" else "normal"
        context['priority'] = priority
        return priority, context

    def explain(self):
        return "Assigned priority to feedback."