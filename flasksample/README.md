# Flaskapp
Flaskアプリケーションのサンプルテンプレート
Alpine Linuxベース  

## コンテナ
- flaskapp  
  Flask起動アプリケーション

## サンプルコード
- app.py  
FlaskアプリケーションのメインApp
- subapp.py  
ブループリント機能で分割しているアプリケーション
- static/templates 
テンプレートエンジンを使ったHTMLレンダリング用ファイル

## 付随ファイル
- Dockerfile  
Dockerファイル
- docker-compose.yaml  
Docker composeのマニフェストファイル
- requirements.txt  
pipでインストールするライブラリーの定義ファイル

## codeディレクトリについて
flaskapp/codeディレクトリは、コンテナ内のcodeにマウントしている為、
ソースコード変更後コンテナのビルド無しで再実行可能  
importしているファイルはFlaskの自動再起動が行われないため、
```docker-compose restart```が必要

## 使用方法
1. docker-compose build  
コンテナイメージのビルド 
2. docker-compose up -d  
コンテナの起動
3. docker-compose logs -f 
Flaskのログを表示
4. 別ターミナルを起動してテストリクエスト実行  
curl --noproxy "*" -L http://127.0.0.1:80/healthCheck
5. ソースコード変更後
```docker-compose restart```でアプリケーションの再起動

 ## テストURIコール
 ```bash
curl --noproxy "*" -L http://127.0.0.1:80/healthCheck
curl --noproxy "*" -L http://127.0.0.1:80/sub/test
curl --noproxy "*" -sS -L -X POST -H "Content-Type: application/json" http://127.0.0.1:80/sub/test  -d @./sample.json
```

## クイックスタート
 - [最小限のアプリケーション](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)
 - [Flaskの簡単な使い方](https://qiita.com/zaburo/items/5091041a5afb2a7dffc8)
