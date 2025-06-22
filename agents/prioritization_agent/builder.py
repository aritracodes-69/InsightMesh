from adk.agent_base import AgentBase

class PrioritizationAgent(AgentBase):
    def __init__(self):
        super().__init__("shared/config.yaml", "prioritization_agent")

