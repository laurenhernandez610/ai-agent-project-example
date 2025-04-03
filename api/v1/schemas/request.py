# ------------------------------------------------------------------------------
# request.py
# ------------------------------------------------------------------------------
# This file defines the expected structure of incoming POST requests
# to the agent endpoint. Pydantic ensures type validation and clean error messages.
# ------------------------------------------------------------------------------

from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    input: str = Field(..., description="The user's input or query for the agent")
