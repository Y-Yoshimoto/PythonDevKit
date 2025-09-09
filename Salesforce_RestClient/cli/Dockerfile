# Yarnインストールコンテナ
FROM node:24-trixie-slim
LABEL maintaner='y-yoshimoto'
# 作業ディレクトリ名指定
ARG WORKDIR_NAME=cli
# 環境変数を設定する
ENV NODE_ENV=development

# 必要なパッケージインストール
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update \
    && apt-get install -y sudo git curl jq openssl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

# 実行ユーザー追加
ARG USERNAME=node
ARG USER_UID=1000
ARG USER_GID=1000

# アプリケーションのディレクトリ作成/権限変更
RUN mkdir -p /$WORKDIR_NAME \
    && chown -R $USERNAME:dialout /$WORKDIR_NAME/
# Salesforce/cliインストール
RUN npm install @salesforce/cli --global \
    && yarn cache clean

# ユーザー変更/作業ディレクトリ変更
WORKDIR /$WORKDIR_NAME
CMD ["tail", "-f", "/dev/null"]