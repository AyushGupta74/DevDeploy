pipeline {

    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = "devdeploy"
        CONTAINER_NAME = "devdeploy1"
    }

    stages {

        stage('Setup Virtual Environment') {

            steps {

                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python --version
                    python -m pip install -r requirements.txt
                '''

            }

        }

        stage('Syntax Check') {

            steps {

                sh '''
                    . .venv/bin/activate
                    python -m py_compile app.py
                '''

            }

        }

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t ${IMAGE_NAME}:latest .'

            }

        }

        stage('Verify Docker Image') {

            steps {

                sh 'docker image inspect ${IMAGE_NAME}:latest'

            }

        }

        stage('Run Docker Container') {

            steps {

                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p 5001:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                '''

            }

        }

        stage('Verify Container') {

            steps {

                sh 'docker ps --filter name=${CONTAINER_NAME}'

            }

        }

        stage('Health Check') {

            steps {

                sh '''
                    sleep 5
                    curl --fail http://localhost:5001
                '''

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