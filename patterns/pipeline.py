from agents import WorkerAgent, ServiceAgent, SupportAgent
from orchestration.state_manager import StateManager


class PipelinePattern:
    """
    Pipeline Pattern — agents run in strict sequence, each feeding the next.

    From Paper 2 (arXiv:2508.01186):
    'Sequential orchestration workflows where output of one agent
     becomes the input context for the next agent in the chain.'

    From Paper 1 (arXiv:2601.13671), Section V-B:
    'Execution unit ensures smooth operation and manages
     task dependencies across workflows.'
    """

    def __init__(self):
        self.state = StateManager()
        # Order is fixed — each stage feeds into the next
        self.pipeline = [WorkerAgent(), ServiceAgent(), SupportAgent()]

    async def run(self, task: str):
        context = {}
        results = []

        for agent in self.pipeline:
            output = await agent.run(task, context)
            # Chain: each agent's output becomes next agent's context
            context[f"{agent.agent_type}_result"] = output.result
            self.state.record("pipeline_step", output.agent_name, output.result)
            results.append(output.dict())

        return {
            "pattern": "pipeline",
            "task": task,
            "steps": results,
            "state_log": self.state.get_log()
        }
