from adk.base_step import BaseStep
class LoggerStep(BaseStep):
    def apply(self, input_data, context):
        print("Logging: ", context)
        return True, context

    def explain(self):
        return "Logged feedback and action result."