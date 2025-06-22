from adk.agent_base import AgentBase

class FeedbackLoggerAgent(AgentBase):
    def __init__(self):
        super().__init__("shared/config.yaml", "feedback_logger_agent")
