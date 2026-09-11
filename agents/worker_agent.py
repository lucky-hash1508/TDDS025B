from typing import Optional
from .base_agent import BaseAgent
from .ai_client import call_claude
from models.schemas import AgentResult


class WorkerAgent(BaseAgent):
    """
    Worker Agent — executes the core task.
    From Paper 1 (arXiv:2601.13671), Section IV:
    'Worker agents are responsible for carrying out well-defined tasks.'
    """

    def __init__(self):
        super().__init__("WorkerAgent", "worker")

    async def run(self, task: str, context: Optional[dict] = None) -> AgentResult:
        context = context or {}

        system_prompt = (
            "You are a specialized Worker Agent in a multi-agent AI system. "
            "Your role is to directly execute and research the given task. "
            "Provide a focused, factual response in 3-4 sentences."
        )
        user_message = f"Task: {task}"

        try:
            result = await call_claude(system_prompt, user_message)
            return AgentResult(
                agent_name=self.name,
                agent_type=self.agent_type,
                result=result,
                status="success"
            )
        except Exception as e:
            return AgentResult(
                agent_name=self.name,
                agent_type=self.agent_type,
                result=f"Worker error: {str(e)}",
                status="error"
            )