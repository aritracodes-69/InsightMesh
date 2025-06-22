from adk.base_step import BaseStep
from tools.rag_tool import query_rag_context

class ExplainerStep(BaseStep):
    def apply(self, input_data, context):
        context_data = query_rag_context(input_data)
        context["rag_context"] = context_data
        return context_data, context

    def explain(self):
        return "Retrieved relevant context using RAG."
