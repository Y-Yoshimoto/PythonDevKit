# FileIO Set
Pythonでのファイル読み書き用コード

## 対象ファイル
  - csv
  - json

## コンテナ
- python  
  Python実行環境

## サンプルコード
- main.py  
main文ファイルのサンプルファイル
- sampleClass.py  
jsonファイルを読み込んで表示させるサンプルクラス
- sampleFunction.py  
時刻表示と文字列表示を行うサンプル関数

## 付随ファイル
- Dockerfile  
Dockerファイル
- docker-compose.yaml  
Docker composeのマニフェストファイル
- .env  
環境変数定義ファイル
- requirements.txt  
pipでインストールするライブラリーの定義ファイル

## srcディレクトリについて
python_dev/srcディレクトリは、コンテナ内の/usr/srcにマウントしている為、
ソースコード変更後、ビルド無しで再実行可能

## 使用方法
1. docker-compose build  
コンテナイメージのビルド 
2. docker-compose up -d  
コンテナの起動
2. docker-compose ps 
コンテナの起動確認
3. docker-compose exec python /bin/ash  
コンテナのシェルにアタッチ
4. python main.py  
main.pyの実行

## ライブラリーの追加方法
コンテナのシェルにアタッチした状態で、pipコマンドを実行する  
```ash
pip install PyMongo
```
インストールに成功したら、"requirements.txt"ファイルに追記し、イメージビルドの実行とコンテナの再起動を行う