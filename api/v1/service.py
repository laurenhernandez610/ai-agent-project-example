# ------------------------------------------------------------------------------
# service.py
# ------------------------------------------------------------------------------
# This module contains the actual business logic for each route in router.py.
# It's a bridge between the API layer and the core agent logic.
#
# This keeps route definitions clean and reusable across web/CLI/dev use.
# ------------------------------------------------------------------------------

from api.v1.schemas.request import AgentRequest
from api.v1.schemas.response import AgentResponse
from src.agents.agent import run_agent

def run_agent_service(request: AgentRequest) -> AgentResponse:
    """
    Handles the API request by calling the appropriate agent logic.
    Converts the result into a validated response schema.
    """
    agent_result = run_agent(user_input=request.input)
    return AgentResponse(**agent_result)
