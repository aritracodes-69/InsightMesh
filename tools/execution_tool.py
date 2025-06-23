# tools/execution_tool.py

def perform_action(action: str) -> str:
    """
    Simulate performing an action and return a status message.

    Args:
        action (str): The action to be performed.

    Returns:
        str: Status message.
    """
    if not action or not isinstance(action, str):
        return "⚠️ No valid action specified."
    action = action.lower()
    if action in ["notify_admin", "send_email"]:
        return f"📧 Notification sent for action '{action}'."
    elif action in ["create_ticket", "open_issue"]:
        return f"🎫 Ticket created for action '{action}'."
    elif action in ["restart_service", "deploy_patch"]:
        return f"🔄 Service restarted or patch deployed for action '{action}'."
    else:
        return f"✅ Action '{action}' performed successfully."
