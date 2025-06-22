from adk.base_step import BaseStep
from tools.execution_tool import perform_action

class ExecuteStep(BaseStep):
    def apply(self, input_data, context):
        result = perform_action("Log Ticket")
        context["execution_result"] = result
        return input_data, context

    def explain(self,context):
        return f"Execution result: {context.get('execution_result', 'None')}"
