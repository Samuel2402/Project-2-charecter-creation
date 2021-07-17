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
                    sh "sudo apt install python3-pip"
                    sh "sudo apt install python3-venv -y"
                    sh "python3 -m venv venv" 
                    sh ". ./venv/bin/activate"
                    sh "pip3 install -r requirements.txt"
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


