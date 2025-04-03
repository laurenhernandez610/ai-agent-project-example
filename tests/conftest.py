# ------------------------------------------------------------------------------
# conftest.py
# ------------------------------------------------------------------------------
# This file defines shared test fixtures and configuration used across multiple
# test files in the test suite. It is automatically discovered by pytest.
#
# Use this to avoid repetition and to share mock data, environments, or clients.
# ------------------------------------------------------------------------------

import pytest
#from fastapi.testclient import TestClient
from api.v1.router import app

@pytest.fixture(scope="module")
def client():
    """Fixture to create a reusable FastAPI test client."""
    #return TestClient(app)

@pytest.fixture
def sample_input():
    """Fixture that returns a minimal example request payload."""
    return {
        "goal": "Plan my tasks for the day",
        "preferences": {"time_blocking": True}
    }
