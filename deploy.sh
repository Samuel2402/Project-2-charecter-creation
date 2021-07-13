#!/bin/bash
project_name=character_api # name must match http link in app  ### cannot have space
# Build server
docker build ${project_name}_server server # refers to dir server
# Build charecter api
docker build -t ${project_name}_api character_api
# Create network
docker network create ${project_name}_network
# Run containers
docker run -d \
    -p 5000:5000 \
    --name ${project_name}_server --network ${project_name}_network \
    ${project_name}_server

docker run -d \
    --name ${project_name}_api \
    --network ${project_name}_network \
    ${project_name}_api