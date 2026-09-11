class Planner:
    """
    Planning Unit — decomposes high-level task into subtasks.
    From Paper 1 (arXiv:2601.13671), Section V-A:
    'The planning unit operates as a goal-decomposition engine
     that determines what tasks need to be done and in what order.'
    """

    def decompose(self, task: str) -> list:
        return [
            {"step": 1, "action": "execute",  "agent": "worker"},
            {"step": 2, "action": "validate",  "agent": "service"},
            {"step": 3, "action": "summarize", "agent": "support"},
        ]
