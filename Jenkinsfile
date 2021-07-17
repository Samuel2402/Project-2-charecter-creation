pipeline{
        agent any
        environment {
            DB_PASSWORD = credential("DB_URI")
        }
        stages{
            stage('Build'){
                steps{
                    sh "sudo docker-compose up -d --build"
                    sh "export DB_URI" 
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
            stage('Deploying'){
                steps{
                    sh "sudo docker stack services stack-1"
                }
            }
        }    
    }
}