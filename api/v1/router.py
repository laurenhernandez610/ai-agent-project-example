# ------------------------------------------------------------------------------
# router.py
# ------------------------------------------------------------------------------
# This file defines the API routes for version 1 of the service.
# It wires together request/response schemas and the underlying service logic.
#
# You run this via:
#   uvicorn api.v1.router:app --reload
#
# In a production app, this router would be registered to a global FastAPI app.
# ------------------------------------------------------------------------------

from fastapi import FastAPI, HTTPException
from api.v1.schemas.request import AgentRequest
from api.v1.schemas.response import AgentResponse
from api.v1.service import run_agent_service

app = FastAPI(title="Agentic AI API", version="1.0")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/query", response_model=AgentResponse)
def query_agent(request: AgentRequest):
    try:
        result = run_agent_service(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
