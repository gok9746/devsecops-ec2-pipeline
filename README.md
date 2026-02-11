# DevSecOps EC2 Pipeline Demo

FastAPI service with CI security gates and container scanning.

## What this repo shows
- Python API + tests
- Linting with Ruff
- Bandit + pip-audit security checks
- Docker build
- Trivy image scan
- Container pushed to GHCR

## Run locally
Run:
docker compose up --build

Then visit:
- http://localhost:8000/docs
- http://localhost:8000/health
