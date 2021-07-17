pipeline{
        agent any
        environment {
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Build'){
                steps{
                    sh "export 'DATABASE_URI'=${DATABASE_URI}"
                    sh "docker pull samuel240210/stats_api" 
                    sh "docker pull samuel240210/race_api:latest"
                    sh "docker pull samuel240210/class_api:latest"
                    sh "docker pull samuel240210/stats_api:latest"
                    sh "sudo apt install python3-pip3"
                    sh "pip install -r requirements.txt"
                }
            }
            stage('Test'){
                steps{
                    sh "cd Project-2-charecter-creation && source venv/bin/activate && cd service-1-server && pytest test.py"
                    sh "cd Project-2-charecter-creation && source venv/bin/activate && cd service-2-race && pytest test.py"
                    sh "cd Project-2-charecter-creation && source venv/bin/activate && cd service-3-class && pytest test.py"
                    sh "cd Project-2-charecter-creation && source venv/bin/activate && cd service-4-stats && pytest test.py"
                }
            }
            stage('Deploy'){
                steps{
                    sh "sudo docker stack services stack-1"
                }
            }
        }    
    }


