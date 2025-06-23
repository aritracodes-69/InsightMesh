import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() 
# Load Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_with_gemini(text: str) -> str:
    """
    Uses Gemini to summarize the input text.
    """
    prompt = f"""
    Summarize the following user feedback in one sentence:

    Feedback: "{text}"
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Summarization Error] {e}")
        return "Could not summarize the feedback."

