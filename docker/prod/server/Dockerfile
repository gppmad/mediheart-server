# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /app_server

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./app_server/requirements /app_server/requirements

RUN pip install --no-cache-dir -r requirements/prod.txt

# copy project
COPY ./app_server /app_server