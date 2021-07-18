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
                    sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd service-1-server && python3 -m pytest test.py"
                    sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd service-2-race && python3 -m pytest test.py"
                    sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd service-3-class && python3 -m pytest test.py"
                    sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd service-4-stats && python3 -m pytest test.py"
                }
            }
            stage('Deploy'){
                steps{
                    sh "docker stack deploy --compose-file docker-compose.yaml stack-1"
                }
            }
        }    
    }
