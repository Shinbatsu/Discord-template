FROM python:3.11.0-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 
RUN mkdir downloads
RUN apt-get update && apt-get install ffmpeg


CMD ["python3","bot.py"]