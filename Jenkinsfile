pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Trayz72/flask-pytest-demo.git'
            }
        }
        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install flask pytest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --junitxml=report.xml
                '''
            }
        }
    }
    post {
        always {
            junit 'report.xml'
        }
    }
}
