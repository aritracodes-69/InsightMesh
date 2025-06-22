# tools/classification.py

def classify_text(text: str) -> str:
    """
    Classify a given text into predefined feedback categories.

    Args:
        text (str): User feedback text.

    Returns:
        str: Category label ('bug_report', 'feature_request', or 'general').
    """
    if not text:
        return "general"

    lowered = text.lower()
    if "error" in lowered or "fail" in lowered or "bug" in lowered:
        return "bug_report"
    elif "feature" in lowered or "add" in lowered:
        return "feature_request"
    return "general"

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_classify_and_prioritize(feedback):
    prompt = f"""
    Analyze this user feedback and respond with a JSON:
    Feedback: "{feedback}"

    Return format:
    {{
      "category": "bug_report" | "feature_request" | "general",
      "priority": "high" | "normal" | "low"
    }}
    """

    model = genai.GenerativeModel("gemini-pro")
    try:
        response = model.generate_content(prompt)
        json_response = eval(response.text.strip())
        return json_response.get("category", "general"), json_response.get("priority", "normal")
    except Exception as e:
        print("Gemini error:", e)
        return "general", "normal"
