# tools/priority_tool.py

def assign_priority(category: str) -> str:
    """
    Assign priority based on feedback category.

    Args:
        category (str): The classified category of feedback.

    Returns:
        str: Priority level ('critical', 'high', 'medium', 'low', or 'normal').
    """
    category = category.lower()
    if category in ["security_issue", "data_loss"]:
        return "critical"
    elif category in ["bug_report", "crash", "performance"]:
        return "high"
    elif category in ["feature_request", "usability"]:
        return "medium"
    elif category in ["question", "general"]:
        return "low"
    else:
        return "normal"