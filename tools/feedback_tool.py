# tools/feedback_tool.py

def preprocess_feedback(feedback: str) -> str:
    """
    Preprocess raw user feedback text.

    Args:
        feedback (str): Raw feedback.

    Returns:
        str: Cleaned and normalized feedback.
    """
    return feedback.strip().lower()

