FROM python:alpine3.16 as base

RUN mkdir /app/
WORKDIR /app/


COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /app/
