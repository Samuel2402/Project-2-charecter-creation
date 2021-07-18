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
                    sh ". ./venv/bin/activate && pip3 install -r requirements.txt && pytest --version && pip3 install Flask-Testing"
                }
            }
            stage('Test'){
                steps{
                    sh "cd service-1-server && python3 -m pytest test.py"
                    sh "cd service-2-race && python3 -m pytest test.py"
                    sh "cd service-3-class && python3 -m pytest test.py"
                    sh "cd service-4-stats && python3 -m pytest test.py"
                }
            }
            stage('Deploy'){
                steps{
                    sh "sudo docker stack services stack-1"
                }
            }
        }    
    }
