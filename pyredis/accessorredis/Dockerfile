# FROM node:latest
FROM python:alpine
LABEL maintaner='y-yoshimoto'

RUN apk --no-cache add python3-dev

### pip
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt && pip freeze > requirements.lock

WORKDIR /usr/src
VOLUME /usr/src

COPY ./src/* ./

#ENTRYPOINT ["python", "main.py"]
ENTRYPOINT ["tail", "-f", "/dev/null"]