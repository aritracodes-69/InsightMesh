# tools/feedback_tool.py

import re

def preprocess_feedback(feedback: str) -> str:
    """
    Preprocess raw user feedback text.

    Args:
        feedback (str): Raw feedback.

    Returns:
        str: Cleaned and normalized feedback.
    """
    if not isinstance(feedback, str):
        return ""
    # Remove leading/trailing whitespace and lowercase
    cleaned = feedback.strip().lower()
    # Remove excessive whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned)
    # Remove non-printable/control characters
    cleaned = re.sub(r'[^\x20-\x7E]', '', cleaned)
    # Optionally, remove common greetings/signatures (example)
    cleaned = re.sub(r'^(hi|hello|dear)[\s,]+', '', cleaned)
    cleaned = re.sub(r'(thanks|regards)[\s,]*$', '', cleaned)
    return cleaned
