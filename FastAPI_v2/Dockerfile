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
COPY ./pythonWatch.sh /usr/local/bin/
RUN echo 'alias py="python"' >> /etc/bash.bashrc \
    && echo 'alias pyw="pythonWatch.sh"' >> /etc/bash.bashrc \
    # && echo 'alias pyt="python -m unittest"' >> /etc/bash.bashrc \
    && echo 'export pyt="python -m pytest"' >> /etc/bash.bashrc \
    && echo 'export pytest="python -m pytest"' >> /etc/bash.bashrc

# Install curl
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl\
    && apt-get -y clean
# Install pip package
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze > requirements.lock 
EXPOSE 8000

# COPY ./src/* /usr/src
WORKDIR /usr/src/

## unicon起動用
# CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
## Gunicorn起動用
# CMD ["gunicorn" ,"--config", "gunicorn.conf.py"]
## デバック用
CMD [ "tail", "-f", "/dev/null"]
