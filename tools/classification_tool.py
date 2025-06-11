# Placeholder for classification_tool.py
def classify_text(text):
    if "error" in text:
        return "bug_report"
    elif "feature" in text:
        return "feature_request"
    return "general"