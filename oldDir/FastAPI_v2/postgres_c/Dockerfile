# https://hub.docker.com/_/postgres
# postgres:17テンプレート
FROM postgres:17-bookworm 
LABEL maintainer="y.yoshimoto"

# 設定ファイルのコピー
# sample: /usr/share/postgresql/postgresql.conf.sample
# COPY postgresql.conf /etc/postgresql/postgresql.conf

# 初期構築データのコピー
COPY ./startup.sql /docker-entrypoint-initdb.d/startup.sql
