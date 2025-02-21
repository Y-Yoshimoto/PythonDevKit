# FROM node:latest
# ROM python:3.10.5-slim-bullseye AS builder
FROM python:3.13-slim-bookworm AS builder
LABEL maintaner='y-yoshimoto'
## Document
# https://detectron2.readthedocs.io/en/latest/tutorials/install.html
## Install build tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends git gcc g++\
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates
RUN pip install --upgrade pip \
    && pip install --no-cache-dir torch torchvision setuptools wheel Cython\
    && pip freeze > requirements.lock
# Build pycocotools
RUN pip download --no-dependencies pycocotools \
    && mkdir -p pycocotools && tar -xvf ./pycocotools-*.tar.gz -C pycocotools --strip-components 1
WORKDIR /pycocotools
RUN python setup.py bdist_wheel \
    && cp /pycocotools/dist/pycocotools-*.whl /tmp/
# Build detectron2
# WORKDIR /
# RUN git clone https://github.com/facebookresearch/detectron2.git
# WORKDIR /detectron2
# RUN python setup.py bdist_wheel && cp /detectron2/dist/detectron2-*.whl /tmp/


# Run Images
FROM python:3.13-slim-bookworm
# FROM python:3.10.5-slim-bullseye
COPY --from=builder /tmp/*.whl /tmp/
# Install OpenCV lib
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # libopencv-dev libgl1-mesa-dev \
    sudo inotify-tools \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates

### Python用短縮コマンド/ホットリロードシェルスクリプトを追加
### PYTHONPATH に共有ライブラリ用のパスを追加
COPY ./pythonWatch.sh /usr/local/bin/
RUN echo 'alias py="python"' >> /etc/bash.bashrc \
    && echo 'alias pyw="pythonWatch.sh"' >> /etc/bash.bashrc \
    && echo 'alias pyt="python -m unittest"' >> /etc/bash.bashrc \
    && echo 'export PYTHONPATH="/usr/src/shared:$PYTHONPATH"' >> /etc/bash.bashrc

# Install pip package
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir /tmp/pycocotools-*.whl \
    # && pip install --no-cache-dir /tmp/detectron2-*.whl \
    && pip freeze > requirements.lock \
    WORKDIR /usr/src

# 実行ユーザー追加
ARG USERNAME=vscode
ARG USER_UID=501
ARG USER_GID=20
RUN useradd -m -s /bin/bash -u $USER_UID -g $USER_GID $USERNAME \
    && usermod -a -G 0 $USERNAME \
    && mkdir -p /vscode/vscode-server/ \
    && chown $USERNAME:dialout /vscode/vscode-server/.*

# COPY ./src/* /usr/src
WORKDIR /usr/src/
VOLUME /usr/src

#ENTRYPOINT ["python", "main.py"]
ENTRYPOINT ["tail", "-f", "/dev/null"]