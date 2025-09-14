pipeline {
    agent any
    stages {

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install --upgrade pip
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                venv/bin/pytest -v --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                sh '''
                # Start Flask in background
                nohup venv/bin/python app.py > flask.log 2>&1 &
                FLASK_PID=$!
                sleep 5  # wait for Flask to start

                # Run Selenium tests
                venv/bin/pytest -v test_ui.py

                # Stop Flask server
                kill $FLASK_PID
                '''
            }
        }
    }
}
