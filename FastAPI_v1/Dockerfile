# Run Images
FROM python:3.10-slim-bullseye
# Install curl
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl\
    && apt-get -y clean
# Install pip package
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze > requirements.lock 
EXPOSE 5000

COPY ./src/* /usr/src
WORKDIR /usr/src/

## unicon起動用
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
## Gunicorn起動用
#CMD ["gunicorn" ,"--config", "gunicorn.conf.py"]
## デバック用
#CMD [ "tail", "-f", "/dev/null"]
