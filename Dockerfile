FROM python:3.7-alpine
MAINTAINER diwdow

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src

RUN adduser -D diwdow
USER diwdow

#docker build -t <name images>[djangogit] .