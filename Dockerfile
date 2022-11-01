FROM python:3.8-buster as base

RUN mkdir /app/
WORKDIR /app/

RUN pip install --upgrade pip
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /app/

# ENV FLASK_APP=server.py