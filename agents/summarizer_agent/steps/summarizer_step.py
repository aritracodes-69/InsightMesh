from adk.base_step import BaseStep
from tools.summarizer_tool import summarize_with_gemini

class SummarizationStep(BaseStep):
    def apply(self, input_data, context):
        """
        Generate a summary of the cleaned feedback using Gemini and update the context.
        """
        cleaned_feedback = context.get("cleaned_feedback", input_data)
        summary = summarize_with_gemini(cleaned_feedback)
        context["summary"] = summary
        return input_data, context

    def explain(self):
        return "Generated a summary of the feedback using Gemini."




