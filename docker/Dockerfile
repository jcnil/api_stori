FROM python:3.9.16-alpine

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y gcc python3-dev \
  && apt-get -y install libffi-dev

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt
RUN pip install --upgrade pip

COPY . /app/



