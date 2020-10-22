FROM python:3.8.6-buster

WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . .

