FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

