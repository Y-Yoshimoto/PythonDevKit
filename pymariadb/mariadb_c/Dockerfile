FROM mariadb
LABEL maintaner='y-yoshimoto'

# 設定ファイルのコピー
COPY my.cnf /etc/mysql/my.cnf

# ポートエクスポート
EXPOSE 3306
# 初期構築データのコピー
COPY setupSQL/startup.sql /docker-entrypoint-initdb.d/startup.sql
