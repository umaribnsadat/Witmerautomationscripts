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
                // Install dependencies from requirements.txt using Python 3.12.3
                bat '"C:\\Users\\umarh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('Run Automation Script') {
            steps {
                // Directly reference the Python script
                bat '"C:\\Users\\umarh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" anxiety.py'
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
