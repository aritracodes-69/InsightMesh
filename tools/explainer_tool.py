from adk.base_step import BaseStep
from tools.rag_tool import query_rag_context

class ExplainerStep(BaseStep):
    def apply(self, input_data, context):
        rag_result = query_rag_context(input_data)
        context["rag_context"] = rag_result
        return input_data, context

    def explain(self,context):
        return context.get("rag_context", "No RAG context retrieved.")

