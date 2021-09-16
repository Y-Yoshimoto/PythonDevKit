# build
FROM python:alpine
# https://hub.docker.com/r/library/python
LABEL  maintainer "y.yoshimoto"

# pip
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt && pip freeze > requirements.lock
RUN mkdir /code
COPY . /code/
WORKDIR /code
## 通常起動用
#CMD [ "flask", "run", "--host=0.0.0.0"]
## デバッグ起動用
CMD [ "flask", "run", "--host=0.0.0.0", "--debugger", "--reload"]
## 検証用
#CMD [ "tail", "-f", "/dev/null"]