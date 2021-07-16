#!/bin/bash
project_name=character_creation # name must match http link in app  ### cannot have space
# Build server
docker build --tag ${project_name}_server server # refers to dir server
# Build race api
docker build -t ${project_name}_api race_api -f ./service-1-server app.py
# Build class api
docker build -t ${project_name}_api class_api -f ./service-2-race app.py
# Build stats api
docker build -t ${project_name}_api stats_api -f ./service-3-class app.py
# Create network
docker network create ${project_name}_network -f ./service-4-stats app.py
# Run containers
docker run -d \
    -p 5000:5000 \
    --name ${project_name}_server --network ${project_name}_network \
    ${project_name}_server

docker run -d \
    --name ${project_name}_api \
    --network ${project_name}_network \
    ${project_name}_api