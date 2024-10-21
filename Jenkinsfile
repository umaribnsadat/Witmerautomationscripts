pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/umaribnsadat/Witmerautomationscripts.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\umarh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('Run Automation Script') {
            steps {
                // Directly reference the Python script (no subfolder needed)
                bat '"C:\\Users\\umarh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" case20-ve.py'
            }
        }
    }
    post {
        success {
            echo 'Automation script executed successfully!'
        }
        failure {
            echo 'Script execution failed!'
        }
    }
}
