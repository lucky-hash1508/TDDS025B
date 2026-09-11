import asyncio
from agents import WorkerAgent, ServiceAgent, SupportAgent
from orchestration.state_manager import StateManager


class ParallelPattern:
    """
    Parallel Pattern — all agents execute simultaneously, results merged.

    From Paper 2 (arXiv:2508.01186):
    'Multi-agent collaboration includes parallel execution
     where agents independently process tasks concurrently.'

    From Paper 1 (arXiv:2601.13671), Section V-B:
    'The control unit manages concurrency and dependency across workflows,
     allowing parallel execution and synchronization at key checkpoints.'
    """

    def __init__(self):
        self.state = StateManager()
        self.agents = [WorkerAgent(), ServiceAgent(), SupportAgent()]

    async def run(self, task: str):
        # All agents run at the SAME time — no context sharing between them
        outputs = await asyncio.gather(*[
            agent.run(task, {}) for agent in self.agents
        ])

        results = []
        for output in outputs:
            self.state.record("parallel_exec", output.agent_name, output.result)
            results.append(output.dict())

        return {
            "pattern": "parallel",
            "task": task,
            "results": results,
            "state_log": self.state.get_log()
        }
