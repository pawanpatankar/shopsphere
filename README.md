# ShopSphere - Microservices Demo (Python + GitHub Actions)

This lightweight demo simulates a microservices system and a reusable CI/CD workflow (to practice the "100+ components" pattern).

## What you get
- 4 microservices (Flask): user, product, order, notification
- 1 shared library: `common-lib`
- Dockerfiles and a `docker-compose.yml` to run locally
- GitHub Actions reusable workflow: `.github/workflows/reusable-deploy.yml`
- Per-service workflow callers in `.github/workflows/`

## Run locally (requirements)
- Docker & Docker Compose

### Steps
1. From the project root, build and run:
```bash
docker compose up --build
```
2. Visit services:
- http://localhost:5001 -> user-service
- http://localhost:5002 -> product-service
- http://localhost:5003 -> order-service
- http://localhost:5004 -> notification-service

## Simulating Deployments with GitHub Actions
- The reusable workflow is located at `.github/workflows/reusable-deploy.yml`.
- Each service has a small workflow that `uses` the reusable workflow.
- In a real GitHub repo you'd push and the workflow would run. The reusable workflow currently simulates build/deploy steps.

## Next steps (suggestions)
- Replace simulated steps with real Docker image builds and pushes (use GitHub Packages or Docker Hub)
- Add environment-specific secrets and approvals for PROD
- Add unit tests and integration tests to the workflows
- Convert simulated "deploy" step to call a real deployment target (k8s, cloud provider, etc.)

