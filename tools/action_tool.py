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
    if not category or not isinstance(category, str):
        return "No valid category provided for explanation."
    if not priority or not isinstance(priority, str):
        return "No valid priority provided for explanation."

    category = category.lower()
    priority = priority.lower()

    category_descriptions = {
        "security_issue": "a potential security vulnerability that may put user data or system integrity at risk",
        "data_loss": "an incident where user or system data could be lost or corrupted",
        "crash": "an unexpected application crash or freeze affecting usability",
        "performance": "a performance-related issue such as slowness or lag",
        "usability": "a usability concern making the application hard or confusing to use",
        "feature_request": "a suggestion for a new feature or improvement",
        "bug_report": "a report of a malfunction or error in the application",
        "question": "a user inquiry or request for information",
        "general": "general feedback or comments from the user"
    }

    priority_descriptions = {
        "critical": "This requires immediate attention due to its high impact.",
        "high": "This should be addressed soon as it significantly affects users.",
        "medium": "This is important but not urgent.",
        "low": "This can be addressed at a later time.",
        "normal": "This does not require urgent action."
    }

    cat_desc = category_descriptions.get(category, f"an unspecified category ('{category}')")
    pri_desc = priority_descriptions.get(priority, f"with an unspecified priority ('{priority}')")

    return f"The feedback is categorized as {cat_desc} and has been assigned a '{priority}' priority. {pri_desc}"

