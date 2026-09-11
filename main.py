from fastapi import FastAPI
from routes.orchestration import router

app = FastAPI(
    title="Multi-Agent AI Orchestration API",
    description="""
## Architectural Patterns for Multi-Agent AI Orchestration APIs

A FastAPI project implementing three core orchestration patterns grounded in research.

### Reference Papers
- **Paper 1:** *The Orchestration of Multi-Agent Systems* — arXiv:2601.13671
- **Paper 2:** *A Survey on Agent Workflow: Status and Future* — arXiv:2508.01186

### Agent Types (Paper 1, Section IV)
| Agent | Role |
|---|---|
| **WorkerAgent** | Executes core tasks using AI |
| **ServiceAgent** | Validates and quality-checks Worker output |
| **SupportAgent** | Monitors and produces final consolidated summary |

### Orchestration Patterns
| Pattern | Description |
|---|---|
| **Supervisor** | Central orchestrator delegates to agents in sequence |
| **Pipeline** | Each agent's output feeds the next agent's input |
| **Parallel** | All agents execute simultaneously, results merged |

### How to Use
Send a POST request to any pattern endpoint with:
```json
{ "task": "Your task here", "pattern": "supervisor" }
```
    """,
    version="1.0.0"
)

app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    return {
        "project": "Multi-Agent AI Orchestration API",
        "version": "1.0.0",
        "patterns": ["supervisor", "pipeline", "parallel"],
        "agent_types": ["worker", "service", "support"],
        "docs": "/docs",
        "paper_1": "https://arxiv.org/abs/2601.13671",
        "paper_2": "https://arxiv.org/abs/2508.01186"
    }
