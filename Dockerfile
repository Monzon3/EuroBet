FROM python:3.9 AS build
COPY ./requirements.txt /requirements.txt
RUN pip install -r ./requirements.txt
RUN rm /requirements.txt 
COPY ./app /app
WORKDIR /app