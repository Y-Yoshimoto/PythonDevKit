-- Postgresql　初期データ投入サンプル
-- このファイルは、PostgreSQLの初期データ投入サンプルです。

-- データベースの作成
CREATE DATABASE sampledb;

-- データベースの切り替え
\c sampledb

-- テーブルの作成
CREATE TABLE sample_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

-- データの投入
INSERT INTO sample_table (name, age) VALUES ('Alice', 20);
-- バルクでのデータの投入
INSERT INTO sample_table (name, age) VALUES ('Bob', 30), ('Charlie', 40);

-- テーブルのデータを取得
SELECT * FROM sample_table;