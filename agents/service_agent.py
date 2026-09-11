from typing import Optional
from .base_agent import BaseAgent
from .ai_client import call_claude
from models.schemas import AgentResult


class ServiceAgent(BaseAgent):
    """
    Service Agent — validates and quality-checks worker output.
    From Paper 1 (arXiv:2601.13671), Section IV:
    'Service agents provide shared operational capabilities —
     quality assurance, compliance enforcement, diagnostics.'
    """

    def __init__(self):
        super().__init__("ServiceAgent", "service")

    async def run(self, task: str, context: Optional[dict] = None) -> AgentResult:
        context = context or {}
        worker_output = context.get("worker_result", "No prior output available.")

        system_prompt = (
            "You are a specialized Service Agent in a multi-agent AI system. "
            "Your role is to validate, quality-check, and improve the Worker Agent's output. "
            "Point out any gaps, inaccuracies, or improvements in 2-3 sentences."
        )
        user_message = (
            f"Original task: {task}\n\n"
            f"Worker Agent's output to validate:\n{worker_output}"
        )

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
                result=f"Service error: {str(e)}",
                status="error"
            )