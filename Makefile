# ------------------------------------------------------------------------------
# Makefile
# ------------------------------------------------------------------------------
# This file defines shortcut commands to simplify common project operations.
# Run commands like `make run` or `make test` to avoid typing full CLI commands.
#
# Used for local development, testing, code formatting, and Docker workflows.
# ------------------------------------------------------------------------------

# Run the agent CLI directly (bypasses API server)
run:
	python main.py

# Start the FastAPI app with auto-reload for development
api:
	uvicorn api.v1.router:app --reload

# Run the test suite using pytest
test:
	pytest tests/

# Auto-format the code using Black and sort imports using isort
format:
	black . && isort .

# Lint the code using flake8 to enforce style and catch errors
lint:
	flake8 .

# Build the Docker image with the project code
docker-build:
	docker build -t ai-agent .

# Run the Docker container and expose the app on port 8000
docker-run:
	docker run -p 8000:8000 ai-agent
