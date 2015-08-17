# base image from python 2.7
FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/

RUN adduser --disabled-password --gecos '' myuser
