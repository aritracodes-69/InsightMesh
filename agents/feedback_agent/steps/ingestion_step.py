from adk.base_step import BaseStep

class IngestionStep(BaseStep):
    def apply(self, input_data, context):
        context['feedback'] = input_data.strip()
        return context['feedback'], context

    def explain(self):
        return "Ingested raw feedback."
