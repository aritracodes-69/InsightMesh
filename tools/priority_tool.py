# tools/priority_tool.py

def assign_priority(category: str) -> str:
    """
    Assign priority based on feedback category.

    Args:
        category (str): The classified category of feedback.

    Returns:
        str: Priority level ('high' for bug_report, else 'normal').
    """
    return "high" if category == "bug_report" else "normal"
