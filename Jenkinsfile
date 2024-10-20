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
                // Installs dependencies (if any)
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Automation Script') {
            steps {
                // Runs your Python automation script
                bat 'python your_script.py'
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
 
