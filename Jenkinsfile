pipeline{
        agent any
        environment {
            DB_PASSWORD = credentials("DB_URI")
        }
        stages{
            stage('Build'){
                steps{
                    sh "docker-compose build"
                    sh "export DB_PASSWORD" 
                }
            }
            stage('Test'){
                steps{
                    sh "cd service-1-server && pytest test.py"
                    sh "cd service-2-race && pytest test.py"
                    sh "cd service-3-class && pytest test.py"
                    sh "cd service-4-stats && pytest test.py"
                }
            }
            stage('Deploy'){
                steps{
                    sh "sudo docker stack services stack-1"
                }
            }
        }    
    }


