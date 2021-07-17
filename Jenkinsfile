pipeline{
        agent any
        environment {
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Build'){
                steps{
                    sh "export 'DATABASE_URI'=${DATABASE_URI}"
                    sh "docker-compose build"    
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


