from adk.agent_base import AgentBase

class ActionMapperAgent(AgentBase):
    def __init__(self):
        super().__init__("shared/config.yaml", "action_mapper_agent")
