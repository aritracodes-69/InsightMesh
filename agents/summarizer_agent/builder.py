# agents/summarizer_agent/builder.py

from adk.agent_base import AgentBase
from agents.summarizer_agent.steps.summarizer_step import SummarizerStep

class SummarizerAgent(AgentBase):
    def __init__(self):
        super().__init__("shared/config.yaml", "summarizer_agent")
        self.steps = [SummarizerStep()]
