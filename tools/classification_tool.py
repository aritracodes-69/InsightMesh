import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def classify_text(text: str) -> str:
    """
    Classify a given text into predefined feedback categories.

    Args:
        text (str): User feedback text.

    Returns:
        str: Category label ('bug_report', 'feature_request', 'security_issue', 'data_loss', 'crash', 'performance', 'usability', 'question', or 'general').
    """
    if not text:
        return "general"

    lowered = text.lower()
    if any(word in lowered for word in ["security", "vulnerability", "hack", "breach"]):
        return "security_issue"
    elif any(word in lowered for word in ["data loss", "lost data", "missing data"]):
        return "data_loss"
    elif any(word in lowered for word in ["crash", "stopped working", "freeze"]):
        return "crash"
    elif any(word in lowered for word in ["slow", "lag", "performance"]):
        return "performance"
    elif any(word in lowered for word in ["usability", "hard to use", "confusing"]):
        return "usability"
    elif any(word in lowered for word in ["feature", "add", "request"]):
        return "feature_request"
    elif any(word in lowered for word in ["error", "fail", "bug"]):
        return "bug_report"
    elif any(word in lowered for word in ["how", "what", "why", "question", "help"]):
        return "question"
    return "general"

def gemini_classify_and_prioritize(feedback):
    prompt = f"""
    Analyze this user feedback and respond with a JSON:
    Feedback: "{feedback}"

    Return format:
    {{
      "category": "bug_report" | "feature_request" | "security_issue" | "data_loss" | "crash" | "performance" | "usability" | "question" | "general",
      "priority": "critical" | "high" | "medium" | "low" | "normal"
    }}
    """

    model = genai.GenerativeModel("gemini-2.5-pro")
    try:
        response = model.generate_content(prompt)
        json_response = eval(response.text.strip())
        return json_response.get("category", "general"), json_response.get("priority", "normal")
    except Exception as e:
        print("Gemini error:", e)
        return "general", "normal"
