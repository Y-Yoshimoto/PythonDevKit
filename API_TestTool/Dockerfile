# Run Images
FROM python:3.13-slim-bookworm

# vscodeのユーザーを追加
# 実行ユーザー追加
ARG USERNAME=vscode
ARG USER_UID=501
ARG USER_GID=20
RUN useradd -m -s /bin/bash -u $USER_UID -g $USER_GID $USERNAME \
    && usermod -a -G 0 $USERNAME \
    && mkdir -p /vscode/vscode-server/ \
    && chown $USERNAME:dialout /vscode/vscode-server/.*

### Python用短縮コマンド/ホットリロードシェルスクリプトを追加
COPY ./tools/pythonWatch.sh /usr/local/bin/
RUN echo 'alias py="python"' >> /etc/bash.bashrc \
    && echo 'alias pyw="pythonWatch.sh"' >> /etc/bash.bashrc \
    && echo 'export pyt="python -m pytest"' >> /etc/bash.bashrc \
    && echo 'export pytest="python -m pytest"' >> /etc/bash.bashrc

# Install curl
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update \
    && apt-get install -y --no-install-recommends sudo curl postgresql-client inotify-tools\
    && apt-get -y clean

# Install pip package
# https://playwright.dev/python/docs/browsers
RUN mkdir -p /app/src
WORKDIR /app/
COPY requirements.txt /app/
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip \
    pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pytest-playwright \
    && playwright install-deps \
    && pip freeze > requirements.lock

# vscode権限でplaywrightのブラウザをインストール
# ENV PLAYWRIGHT_BROWSERS_PATH=/home/vscode/pw-browsers
RUN sudo -u $USERNAME python -m playwright install chromium
EXPOSE 8000

## unicon起動用
# CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
## Gunicorn起動用
# CMD ["gunicorn" ,"--config", "./src/gunicorn.conf.py"]
## デバック用
CMD [ "tail", "-f", "/dev/null"]
