pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Clone your GitHub repository
                git branch: 'main', url: 'https://github.com/umaribnsadat/Witmerautomationscripts.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                bat '"C:\\Users\\umarh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('Run Automation Script') {
            steps {
                // Ensure the correct script name is specified here
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
