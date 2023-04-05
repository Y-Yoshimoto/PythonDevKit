FROM python:3.11-bullseye
LABEL maintaner='y-yoshimoto'

# Install ffmpeg
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates

# Copy requirements.txt
COPY requirements.txt ./
# Install pip package
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze > requirements.lock

# Make file directory
RUN mkdir -p /usr/src
WORKDIR /usr/src

# CMD tail
CMD ["tail", "-f", "/dev/null"]