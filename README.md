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


## Live Demo
API Docs:
http://54.90.149.12:8000/docs

Health Check:
http://54.90.149.12:8000/health

