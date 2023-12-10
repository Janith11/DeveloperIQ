FROM python:3.8.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r app/requirements.txt

EXPOSE 8002
EXPOSE 8001
