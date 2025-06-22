# tools/action_tool.py

def generate_explanation(category: str, priority: str) -> str:
    """
    Generate a human-readable explanation based on feedback category and priority level.

    Args:
        category (str): The classified category of feedback (e.g., bug, feature request).
        priority (str): The priority level assigned (e.g., high, medium, low).

    Returns:
        str: An explanation summarizing the classification and urgency.
    """
    if not category or not priority:
        return "Insufficient data to generate explanation."

    return f"The feedback is categorized as '{category}' with a '{priority}' priority level."

