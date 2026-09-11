from abc import ABC, abstractmethod
from typing import Optional
from models.schemas import AgentResult


class BaseAgent(ABC):
    def __init__(self, name: str, agent_type: str):
        self.name = name
        self.agent_type = agent_type  # worker / service / support

    @abstractmethod
    async def run(self, task: str, context: Optional[dict] = None) -> AgentResult:
        pass