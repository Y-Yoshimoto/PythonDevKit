# DecodeBase64
  XMLファイルの読み込みとそれに含まれているBase64のファイルを取り出すサンプルコード

## コンテナ
- decodebase64  
  Python実行環境

## サンプルコード
- main.py  
main文ファイルのサンプルファイル

## 付随ファイル
- Dockerfile  
Dockerファイル
- docker-compose.yaml  
Docker composeのマニフェストファイル
- .env  
環境変数定義ファイル
- requirements.txt  
pipでインストールするライブラリーの定義ファイル
- sample.xml
base64文字列を含むサンプルXML
- sample2.xml
base64でエンコードされたファイルを含むサンプルXML
inputfileに元データ

## srcディレクトリについて
DecodeBase64/srcディレクトリは、コンテナ内の/usr/srcにマウントしている為、
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

## Base64のシェルスクリプトでの変換/テストデータ作成
### 文字列のBase64変換/復号
```bash
  echo -n "base64変換と復号" | base64
  echo -n "YmFzZTY05aSJ5o+b44Go5b6p5Y+3" | base64 -d
```
### ファイルのBase64変換/復号
```bash
  # テキストファイル
  cat ./test1file.txt | base64 > B64_test1file
  cat ./B64_test1file | base64 -d > dB64_test1file.txt
  # 画像ファイル
  cat ./test2file.jpg | base64 > B64_test2file
  cat ./B64_test2file | base64 -d > dB64_test2file.jpg
  # PDFファイル
  cat ./test3file.pdf | base64 > B64_test3file
  cat ./B64_test3file | base64 -d > dB64_test3file.pdf
```