from adk.base_step import BaseStep
from tools.logger_tool import log_to_db

class LoggerStep(BaseStep):
    def apply(self, input_data, context):
        log_data = {
            "feedback": input_data,
            "category": context.get("category"),
            "priority": context.get("priority")
        }
        log_to_db(log_data)
        return input_data, context

    def explain(self):
        return "Feedback successfully logged."
