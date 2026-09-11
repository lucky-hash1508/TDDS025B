from fastapi import APIRouter, HTTPException
from models.schemas import TaskRequest
from patterns.supervisor import SupervisorPattern
from patterns.pipeline import PipelinePattern
from patterns.parallel import ParallelPattern

router = APIRouter(prefix="/orchestrate", tags=["Orchestration Patterns"])


@router.post("/supervisor")
async def supervisor_endpoint(request: TaskRequest):
    """
    Supervisor Pattern: Central orchestrator delegates tasks to
    Worker → Service → Support agents in a controlled sequence.
    Each agent's output is passed as context to the next.
    """
    try:
        return await SupervisorPattern().run(request.task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/pipeline")
async def pipeline_endpoint(request: TaskRequest):
    """
    Pipeline Pattern: Agents execute in a strict chain.
    Output of each agent becomes the input of the next agent.
    Worker → Service → Support (sequential chaining).
    """
    try:
        return await PipelinePattern().run(request.task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/parallel")
async def parallel_endpoint(request: TaskRequest):
    """
    Parallel Pattern: All three agents execute simultaneously
    and independently. Results are merged at the end.
    Worker || Service || Support (concurrent execution).
    """
    try:
        return await ParallelPattern().run(request.task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/patterns")
async def list_patterns():
    """Lists all available orchestration patterns and their descriptions."""
    return {
        "patterns": [
            {
                "name": "supervisor",
                "endpoint": "/orchestrate/supervisor",
                "description": "Central orchestrator with sequential agent delegation",
                "paper_ref": "arXiv:2601.13671, Section V"
            },
            {
                "name": "pipeline",
                "endpoint": "/orchestrate/pipeline",
                "description": "Sequential chained execution, output feeds next agent",
                "paper_ref": "arXiv:2508.01186, Workflow Orchestration Flows"
            },
            {
                "name": "parallel",
                "endpoint": "/orchestrate/parallel",
                "description": "Concurrent execution of all agents simultaneously",
                "paper_ref": "arXiv:2601.13671, Section V-B; arXiv:2508.01186"
            }
        ]
    }
