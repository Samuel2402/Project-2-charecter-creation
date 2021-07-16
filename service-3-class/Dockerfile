# Dockerfile for service 3
FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask
RUN pip install requests
ENTRYPOINT ["python3", "app.py"]