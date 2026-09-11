from datetime import datetime


class StateManager:
    """
    State & Knowledge Management.
    From Paper 1 (arXiv:2601.13671), Section V-C:
    'The state unit manages checkpoints, workflow progress,
     agent states, and activity logs.'
    Also from Paper 2 (arXiv:2508.01186):
    'Architectural features include orchestration flows
     and specification languages.'
    """

    def __init__(self):
        self.log = []

    def record(self, step: str, agent: str, result: str):
        self.log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "step": step,
            "agent": agent,
            "result_preview": result[:120] + "..." if len(result) > 120 else result
        })

    def get_log(self):
        return self.log
