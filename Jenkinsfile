pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Clones the code from the GitHub repository
                git branch: 'master', url: 'https://github.com/umaribnsadat/Witmerautomationscripts.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Use the full path to python to install dependencies using pip
                bat '"C:\\Users\\umarh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('Run Automation Script') {
            steps {
                // Use the full path to python to run the automation script
                bat '"C:\\Users\\umarh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" your_script.py'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Script execution failed!'
        }
    }
}
