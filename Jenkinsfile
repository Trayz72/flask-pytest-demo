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
                expression { currentBuild.currentResult == null || currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                script {
                    sh '''
                    # Start Flask app in background
                    export FLASK_ENV=testing
                    nohup venv/bin/python -c "
import sys
sys.path.insert(0, '.')
from app import app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
" > flask.log 2>&1 &
                    
                    # Store the PID
                    FLASK_PID=$!
                    echo "Flask started with PID: $FLASK_PID"
                    
                    # Wait for Flask to start
                    sleep 10
                    
                    # Check if Flask is running
                    curl -f http://localhost:5000 || (echo "Flask not responding" && cat flask.log && exit 1)
                    
                    # Run UI tests
                    venv/bin/pytest -v test_ui.py -s
                    
                    # Kill Flask process
                    kill $FLASK_PID || true
                    sleep 2
                    
                    # Force kill if still running
                    kill -9 $FLASK_PID 2>/dev/null || true
                    '''
                }
            }
            post {
                always {
                    sh '''
                    # Cleanup any remaining Flask processes
                    pkill -f "python.*app.py" || true
                    pkill -f "python.*app" || true
                    '''
                    
                    // Archive Flask logs for debugging
                    archiveArtifacts artifacts: 'flask.log', allowEmptyArchive: true
                }
            }
        }
    }
    
    post {
        always {
            // Clean up any Chrome processes that might be left behind
            sh '''
            pkill -f chrome || true
            pkill -f chromedriver || true
            rm -rf /tmp/chrome-profile-* || true
            '''
        }
    }
}