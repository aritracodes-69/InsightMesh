from adk.agent_base import AgentBase

class ClassificationAgent(AgentBase):
    def __init__(self):
        super().__init__(config_yaml_path="shared/config.yaml", agent_config_section="classification_agent")
