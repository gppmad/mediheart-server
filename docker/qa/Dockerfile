# pull official base image
FROM python:3.8.0-alpine

# set work directory && environment variables
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
# copy project
COPY ./app_server /app
# install requirements
RUN pip install --no-cache-dir -r /app/requirements/dev.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]