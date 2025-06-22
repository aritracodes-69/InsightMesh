from adk.agent_base import AgentBase

class ExecutionAgent(AgentBase):
    def __init__(self):
        super().__init__("shared/config.yaml", "execution_agent")

