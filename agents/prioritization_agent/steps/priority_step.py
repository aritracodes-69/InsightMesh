from adk.base_step import BaseStep
from tools.priority_tool import assign_priority

class PriorityStep(BaseStep):
    def apply(self, input_data, context):
        category = context.get("category", "")
        priority = assign_priority(category)
        context["priority"] = priority
        return input_data, context

    def explain(self,context):
        return f"Assigned priority: {context.get('priority', 'normal')}"
