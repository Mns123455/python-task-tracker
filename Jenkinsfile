pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-task-tracker .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f python-task-tracker-container || true

                    docker run -d \
                      --restart unless-stopped \
                      -p 5003:5000 \
                      --name python-task-tracker-container \
                      python-task-tracker
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    for i in $(seq 1 15); do
                        if curl -fsS http://localhost:5003/health; then
                            echo "Task Tracker is running"
                            exit 0
                        fi
                        sleep 2
                    done

                    docker logs python-task-tracker-container
                    exit 1
                '''
            }
        }
    }
}
