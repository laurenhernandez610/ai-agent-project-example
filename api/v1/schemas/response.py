# ------------------------------------------------------------------------------
# response.py
# ------------------------------------------------------------------------------
# This file defines the structure of the JSON response returned to clients.
# Ensures a consistent, documented format for all agent results.
# ------------------------------------------------------------------------------

from pydantic import BaseModel

class AgentResponse(BaseModel):
    input: str
    output: str
