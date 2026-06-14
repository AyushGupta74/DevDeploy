pipeline {

    agent any

    stages {

        stage('Checkout Info') {

            steps {

                echo 'Current Workspace:'

                sh 'pwd'

                echo 'Repository Files:'

                sh 'ls -la'

            }

        }

    }

    post {

        always {

            echo 'Pipeline Completed'

        }

    }

}