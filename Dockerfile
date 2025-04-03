# ------------------------------------------------------------------------------
# Dockerfile
# ------------------------------------------------------------------------------
# This Dockerfile defines how to build a container image for the AI Agent project.
# It creates a portable and reproducible environment with all necessary dependencies.
# Suitable for local dev, production deployment, or cloud hosting.
# ------------------------------------------------------------------------------

# 1. Use an official, minimal Python 3.10 image as the base
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all project files into the container
COPY . .

# 4. Upgrade pip and install all required Python packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 5. Optional: Set environment variables (can also use Docker Compose)
ENV ENVIRONMENT=production

# 6. Expose the port FastAPI will run on (Uvicorn default is 8000)
EXPOSE 8000

# 7. Run the FastAPI app using Uvicorn server
CMD ["uvicorn", "api.v1.router:app", "--host", "0.0.0.0", "--port", "8000"]
