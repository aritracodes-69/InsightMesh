from adk.base_step import BaseStep
from tools.action_tool import generate_explanation

class ActionStep(BaseStep):
    def apply(self, input_data, context):
        category = context.get("category", "")
        priority = context.get("priority", "")
        explanation = generate_explanation(category, priority)
        context["action_explanation"] = explanation
        return input_data, context

    def explain(self,context):
        return context.get("action_explanation", "No explanation generated.")

