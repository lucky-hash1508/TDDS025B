from typing import Optional
from .base_agent import BaseAgent
from .ai_client import call_claude
from models.schemas import AgentResult


class SupportAgent(BaseAgent):
    """
    Support Agent — monitors, summarizes, and provides meta-level oversight.
    From Paper 1 (arXiv:2601.13671), Section IV:
    'Support agents operate at a supervisory and analytical level,
     monitoring system behavior and analyzing outcomes.'
    """

    def __init__(self):
        super().__init__("SupportAgent", "support")

    async def run(self, task: str, context: Optional[dict] = None) -> AgentResult:
        context = context or {}
        worker_output = context.get("worker_result", "N/A")
        service_output = context.get("service_result", "N/A")

        system_prompt = (
            "You are a specialized Support Agent in a multi-agent AI system. "
            "Your role is meta-level oversight: summarize what all agents produced, "
            "assess the overall quality, and give a final consolidated answer in 3-4 sentences."
        )
        user_message = (
            f"Original task: {task}\n\n"
            f"Worker Agent output:\n{worker_output}\n\n"
            f"Service Agent validation:\n{service_output}\n\n"
            "Provide a final summary and quality assessment."
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
                result=f"Support error: {str(e)}",
                status="error"
            )