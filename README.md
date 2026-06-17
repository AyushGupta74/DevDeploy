# DevDeploy

A simple Flask demo app with a Jenkins CI/CD pipeline for building, testing, pushing, and running a Docker image.

## Project overview

- `app.py`: Flask application serving a static HTML status page.
- `Dockerfile`: builds the Python container image and runs the Flask app on port `8000`.
- `docker-compose.yml`: starts a Jenkins server with Docker socket access.
- `Jenkinsfile`: defines the CI/CD pipeline for checkout, test, build, verify, push, and run.
- `requirements.txt`: Python dependencies for Flask and pytest.
- `jenkins/Dockerfile`: custom Jenkins image with Docker CLI and Python installed.

## Features

- Local Flask app containerized with Docker
- Jenkins pipeline for automated build/test/deploy
- Docker image pushed to Docker Hub
- Jenkins uses Docker socket mount to build and run containers

## Requirements

- Docker
- Docker Compose
- Jenkins credentials for Docker Hub (`dockerhub-creds`)
- Python 3.11 for local testing (recommended)

## Local development

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Run the app locally:

```bash
python app.py
```

4. Open the app in your browser:

```text
http://localhost:8000
```

## Build and run with Docker

1. Build the Docker image:

```bash
docker build -t devdeploy:local .
```

2. Run the container:

```bash
docker run -p 5001:8000 --name devdeploy-local devdeploy:local
```

3. Access the app:

```text
http://localhost:5001
```

## Jenkins setup

1. Start Jenkins with Docker Compose:

```bash
docker compose up -d
```

2. Open Jenkins:

```text
http://localhost:8080
```

3. Install recommended plugins, including:

- GitHub
- Credentials
- Pipeline

4. Add Docker Hub credentials:

- Credential type: Username with password/token
- ID: `dockerhub-creds`

5. Create or configure a Jenkins pipeline job using the `Jenkinsfile` in this repository.

## Jenkins pipeline stages

- `Checkout Code`: fetches the repository from SCM
- `Run Unit Tests`: creates a `.venv`, installs dependencies, and runs `pytest`
- `Build Docker Image`: builds `devdeploy:latest` and `taskmaster74/devdeploy:${BUILD_NUMBER}`
- `Verify Docker Image`: inspects the built images
- `Push Docker Image`: logs into Docker Hub and pushes the image
- `Run Docker Container`: stops any existing container, then runs the latest image
- `Verify Container`: lists the running container by name

## Notes

- The Flask app listens on `0.0.0.0:8000` inside the container.
- Jenkins requires Docker socket access to build and run container images.
- The pipeline currently uses the Docker Hub username configured in `Jenkinsfile`.
- For GitHub webhook integration, expose Jenkins externally and configure the webhook URL.

## License

This repository does not specify a license. Add one if you plan to share or publish the code.
