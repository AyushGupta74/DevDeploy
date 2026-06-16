FROM jenkins/jenkins:lts

# Run as root to install packages
USER root

# Install Docker CLI, Python 3, curl, and other utilities
RUN apt-get update && \
    apt-get install -y \
    docker.io \
    python3 \
    python3-venv \
    python3-pip \
    curl \
    git \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Switch back to jenkins user
USER jenkins
