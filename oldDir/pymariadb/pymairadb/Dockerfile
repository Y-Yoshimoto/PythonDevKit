# FROM node:latest
FROM python:slim-bullseye
LABEL maintaner='y-yoshimoto'

# apt
RUN apt-get -y update\
    && apt-get install -y gcc libmariadb-dev\
    && apt-get clean

### pip
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt && pip freeze > requirements.lock

WORKDIR /usr/src
VOLUME /usr/src
# COPY python_dev/src/* ./

#ENTRYPOINT ["python", "main.py"]
ENTRYPOINT ["tail", "-f", "/dev/null"]