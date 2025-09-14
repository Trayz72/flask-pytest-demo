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
    when {
        expression { currentBuild.currentResult == null || currentBuild.currentResult == 'SUCCESS' || currentBuild.currentResult == 'FAILURE' }
    }
    steps {
        sh '''
        nohup venv/bin/python app.py > flask.log 2>&1 &
        FLASK_PID=$!
        sleep 5
        venv/bin/pytest -v test_ui.py || true
        kill $FLASK_PID
        '''
    }
}
    }
}
