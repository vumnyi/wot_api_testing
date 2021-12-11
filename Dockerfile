FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y

RUN apt-get install python3.9 -y
RUN apt-get install python3-pip -y


WORKDIR /app
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt