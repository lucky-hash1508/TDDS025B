from pydantic import BaseModel
from typing import Any, Optional
from enum import Enum


class PatternType(str, Enum):
    supervisor = "supervisor"
    pipeline = "pipeline"
    parallel = "parallel"


class TaskRequest(BaseModel):
    task: str
    pattern: PatternType
    context: dict = {}


class AgentResult(BaseModel):
    agent_name: str
    agent_type: str   # worker / service / support
    result: Any
    status: str = "success"


class OrchestrationResponse(BaseModel):
    pattern: str
    task: str
    results: Any
    state_log: list = []
