from adk.agent_base import AgentBase

class FeedbackAgent(AgentBase):
    def __init__(self):
        super().__init__("shared/config.yaml", "feedback_agent")


