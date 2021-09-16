# FROM python:alpine
FROM python:slim-buster
LABEL maintaner='y-yoshimoto'

### pip
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt && pip freeze > requirements.lock

WORKDIR /usr/src
VOLUME /usr/src


# COPY python_dev/src/* ./

#ENTRYPOINT ["python", "main.py"]
ENTRYPOINT ["tail", "-f", "/dev/null"]