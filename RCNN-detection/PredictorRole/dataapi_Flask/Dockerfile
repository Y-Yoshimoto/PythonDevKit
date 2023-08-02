FROM python:3.11-bullseye
# https://hub.docker.com/_/python
LABEL maintaner='y-yoshimoto'

# pip
COPY requirements.txt /
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze > requirements.lock
# uwsgi
COPY app.ini /

COPY /src /usr/src
WORKDIR /usr/src


## 通常起動用
#CMD [ "flask", "run", "--host=0.0.0.0"]
## デバッグ起動用
#CMD [ "flask", "run", "--host=0.0.0.0", "--debugger", "--reload"]

#uwsgi --ini /app.ini &
## 検証用
#CMD [ "tail", "-f", "/dev/null"]
CMD [ "uwsgi", "--ini", "/app.ini"]