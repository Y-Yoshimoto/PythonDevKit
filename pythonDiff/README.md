# Similar Search 
類似度を利用したマスター検索のプロトタイプ

## コンテナ
- similar_search  
  Python実行環境

## Pythonコード
- main.py  
  main文
- subFunctions.py  
  ファイル読み込み/ログ出力用関数

## 付随ファイル
- Master.csv  
  マスターデータサンプル
- searchData.csv  
  検索対象データサンプル
- Similar.csv  
  処理結果サンプルファイル

## 処理説明
1. Master.csv, searchData.csv ファイルの読み込み
2. 類似度を元にマスターデータから検索
3. 検索対象と検索結果の上位を結合しデータ出力データを作成
4. 検索結果をCSVファイルとして出力

## チューニング/調整箇所
  - masterMatch関数:  
    ignoreStr: 検索時に無効化する文字を指定
  - MatchjoinMaster関数:  
    top デフォルト値で上位の何位までを取得するかを指定  
    masterMatchの引数: 検索対象とマスターデータで類似度を測るカラムを指定  
    Similaradd: 出力結果に吐き出すカラムを指定  
  - main:  
    ファイル名: 実際に使用するファイルを指定
    header: CSVに出力するカラムを指定

## 使用方法
1. docker-compose build  
コンテナイメージのビルド 
2. docker-compose up -d  
コンテナの起動
2. docker-compose ps 
コンテナの起動確認
3. docker-compose exec similar_search /bin/bash  
コンテナのシェルにアタッチ
4. python main.py  
main.pyの実行
