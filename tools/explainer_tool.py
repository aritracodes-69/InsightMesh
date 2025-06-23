from adk.base_step import BaseStep
from tools.rag_tool import query_rag_context

class ExplainerStep(BaseStep):
    def apply(self, input_data, context):
        # Retrieve RAG context for the input data
        rag_result = query_rag_context(input_data)
        context["rag_context"] = rag_result
        context["explanation"] = f"RAG context retrieved for input: {input_data}"
        return input_data, context

    def explain(self, context):
        # Provide a detailed explanation if available
        rag_context = context.get("rag_context", "No RAG context retrieved.")
        explanation = context.get("explanation", "")
        return f"{explanation}\n\n{rag_context}" if explanation else rag_context

