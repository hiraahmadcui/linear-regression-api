pipeline {
    agent any

    environment {
        IMAGE = "hiracul/linear-regression-api:latest"
    }

    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $IMAGE'
                }
            }
        }

        stage('Deploy with docker-compose') {
            steps {
                sh 'docker compose down'
                sh 'docker compose pull'
                sh 'docker compose up -d'
            }
        }
    }
}