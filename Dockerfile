FROM ubuntu:latest
MAINTAINER Hanju Jo "dev.hanju.jo@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
COPY . /usr/src/project
WORKDIR /usr/src/project
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["gunicorn --bind localhost:6881 run:app"]