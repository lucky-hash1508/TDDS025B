from agents import WorkerAgent, ServiceAgent, SupportAgent
from orchestration.planner import Planner
from orchestration.state_manager import StateManager


class SupervisorPattern:
    """
    Supervisor Pattern — central orchestrator delegates tasks to agents sequentially.

    From Paper 1 (arXiv:2601.13671), Section V:
    'The orchestration layer interprets system-level objectives,
     decomposes them into actionable subtasks, and coordinates execution.'

    From Paper 2 (arXiv:2508.01186):
    'Orchestration flows define how agents are coordinated
     and how information passes between them.'
    """

    def __init__(self):
        self.planner = Planner()
        self.state = StateManager()
        self.agents = {
            "worker":  WorkerAgent(),
            "service": ServiceAgent(),
            "support": SupportAgent(),
        }

    async def run(self, task: str):
        plan = self.planner.decompose(task)
        results = []
        context = {}

        for step in plan:
            agent = self.agents[step["agent"]]
            output = await agent.run(task, context)

            # Mark failed steps clearly so downstream agents don't treat
            # an error message as valid prior output.
            if output.status == "error":
                context[f"{step['agent']}_result"] = f"[{step['agent']} failed: {output.result}]"
            else:
                context[f"{step['agent']}_result"] = output.result

            self.state.record(step["action"], output.agent_name, output.result)
            results.append(output.dict())

        return {
            "pattern": "supervisor",
            "task": task,
            "results": results,
            "state_log": self.state.get_log()
        }