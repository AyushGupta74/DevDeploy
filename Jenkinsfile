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

        PYENV_ROOT           = '/Users/your_mac_username/.pyenv'
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
                sh "python --version"
                sh "pip install -r requirements.txt"
                sh "pytest" // Uncomment this if you use testing tools
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