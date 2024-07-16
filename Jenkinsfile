pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ShobitPandey/my-python-webapp.git', branch: 'master'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install flask
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    # Add your test commands here
                    echo "No tests yet."
                '''
            }
        }
        stage('Deploy Application') {
            steps {
                sh '''
                    source venv/bin/activate
                    nohup python app.py &
                '''
            }
        }
    }
}

