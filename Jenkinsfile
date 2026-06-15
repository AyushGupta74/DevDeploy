pipeline {

    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        DOCKER_REGISTRY_USER = 'taskmaster74'
        HOST_PORT            = "5001"
        CONTAINER_PORT       = "8000"
        IMAGE_NAME           = "devdeploy"
        IMAGE_TAG            = "${BUILD_NUMBER}"
        FULL_IMAGE_PATH      = "${DOCKER_REGISTRY_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
        CONTAINER_NAME       = "devdeploy1"

        PYENV_ROOT           = "/var/jenkins_home/.pyenv/versions/3.11.0"
        PATH                 = "${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:/usr/local/bin:${env.PATH}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Optional: Verifies your Python code works on 3.11.0 before making a container
                sh """
                    python3 --version
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                    python3 -m pytest --version
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh "docker image inspect ${IMAGE_NAME}:latest"
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p ${HOST_PORT}:${CONTAINER_PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Verify Container') {
            steps {
                sh "docker ps --filter name=${CONTAINER_NAME}"
            }
        }
    }

    post {
        success {
            echo 'Pipeline Succeeded'
        }

        failure {
            echo 'Pipeline Failed'
        }

        always {
            echo 'Pipeline Completed'
        }
    }
}
