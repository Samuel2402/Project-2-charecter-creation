pipeline{
        agent any
        environment {
            DB_PASSWORD = credentials("DB_URI")
        }
        stages{
            stage('Build'){
                steps{
                    sh "curl https://get.docker.com | sudo bash"
                    sh "echo Downloaded Docker"
                    sh "sudo apt install -y curl jq"
                    sh "sudo curl -L 'https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose"
                    sh "sudo chmod +x /usr/local/bin/docker-compose"
                    sh "docker-compose -d --build"
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


