FROM python:slim-bookworm
LABEL maintaner='y-yoshimoto'

# Install apt package
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates inotify-tools \
    && update-ca-certificates

# Install postgresql-client-17
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    install -d /usr/share/postgresql-common/pgdg \
    && curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc \
    --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc \
    && . /etc/os-release \
    && sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list" \
    && install -d /usr/share/postgresql-common/pgdg \
    && curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client-17 

### Python用短縮コマンド/ホットリロードシェルスクリプトを追加
### PYTHONPATH に共有ライブラリ用のパスを追加
COPY ./pythonWatch.sh /usr/local/bin/
RUN echo 'alias py="python"' >> /etc/bash.bashrc \
    && echo 'alias pyw="pythonWatch.sh"' >> /etc/bash.bashrc \
    && echo 'alias pyt="python -m unittest"' >> /etc/bash.bashrc \
    && echo 'export PYTHONPATH="/app/shared:$PYTHONPATH"' >> /etc/bash.bashrc \
    && chmod 755 /usr/local/bin/pythonWatch.sh

### Install pip package
COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze > requirements.lock

# 実行ユーザー追加
ARG USERNAME=vscode
ARG USER_UID=501
ARG USER_GID=20
RUN useradd -m -s /bin/bash -u $USER_UID -g $USER_GID $USERNAME \
    && usermod -a -G 0 $USERNAME \
    && mkdir /app/

# Make workdir
WORKDIR /app/
#RUN chown -R $USERNAME:$USERNAME /app
VOLUME /app/

ENTRYPOINT ["tail", "-f", "/dev/null"]