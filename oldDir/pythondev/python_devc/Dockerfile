FROM python:slim-bookworm
LABEL maintaner='y-yoshimoto'

# Install apt package
RUN apt-get update \
    && apt-get install -y --no-install-recommends sudo\
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates

### Install pip package
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze > requirements.lock

ARG WORKDIR=/app/

# 実行ユーザー追加
ARG USERNAME=vscode
ARG USER_UID=501
ARG USER_GID=20
RUN useradd -m -s /bin/bash -u $USER_UID -g $USER_GID $USERNAME \
    && usermod -a -G 0 $USERNAME

# Make workdir
RUN mkdir -p $WORKDIR \
    && chown -R $USERNAME $WORKDIR
VOLUME $WORKDIR

ENTRYPOINT ["tail", "-f", "/dev/null"]