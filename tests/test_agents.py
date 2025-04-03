# ------------------------------------------------------------------------------
# test_agents.py
# ------------------------------------------------------------------------------
# This file contains unit tests for the core agent logic.
# Focuses on behavior of planner_agent, including valid responses,
# error handling, and tool usage.
# ------------------------------------------------------------------------------

import pytest
from agents.agent import run_planning_agent

def test_agent_runs_without_error():
    """Basic smoke test to ensure the agent loop runs."""
    try:
        run_planning_agent()
    except Exception as e:
        pytest.fail(f"Agent crashed with error: {e}")

def test_agent_output_format():
    """Optional: Check that the output matches expected schema/format."""
    result = run_planning_agent()
    assert isinstance(result, dict)
    assert "plan" in result
