# MongoDB/Flask

## テストリクエスト
### コレクション内の全データ取得
curl --noproxy "*" -X GET -L "http://127.0.0.1:35000/data/Sample1/"
### コレクション内の指定カラムの最大値を取得
curl --noproxy "*" -X GET -L "http://127.0.0.1:35000/data/Sample2/max?column=date"

### サンプルデータ登録を1レコード追加
curl --noproxy "*" -X POST -L "http://127.0.0.1:35000/data/Sample1/one" -d @./SampleData/sample1.json

### サンプルデータ登録を複数レコード追加
curl --noproxy "*" -X POST -L "http://127.0.0.1:35000/data/Sample2/" -d @./SampleData/sample2.json

### インデックスを追加
curl --noproxy "*" -X GET -L "http://127.0.0.1:35000/data/Sample2/addIndex?column=date"

### データ削除
curl --noproxy "*" -X DELETE -L "http://127.0.0.1:35000/data/Sample2/many?column=var&value=1"

### データ更新
curl --noproxy "*" -X PATCH -L "http://127.0.0.1:35000/data/Sample2/" -d @./SampleData/updateSample.json




######### old 
## API
### カラム情報取得
curl --noproxy "*" -L http://127.0.0.1:35000/Columns/Account
### 全データ取得
curl --noproxy "*" -L http://127.0.0.1:35000/data/all/Opportunity

curl --noproxy "*" -L http://127.0.0.1:35000/data/all/LoginHistory

### 期間指定検索
curl --noproxy "*" -L 'http://127.0.0.1:35000/data/period/Opportunity?dateColumn=CreatedDate&startDate=2020-05-27&endDate=2020-05-29'


### パイプライン指定検索
curl --noproxy "*" -L http://127.0.0.1:35000/data/pipeline/sample

### 結合データ取得
curl --noproxy "*" -sS -L -X POST -H "Content-Type: application/json" http://127.0.0.1:35000/data/join  -d @./accessormongo/code/datajoinTest.json

### 期間指定
curl --noproxy "*" -sS -L -X POST -H "Content-Type: application/json" http://127.0.0.1:35000/data/period/join  -d @./accessormongo/code/datajoinTest.json

### パイプライン指定検索
curl --noproxy "*" -sS -L -X POST -H "Content-Type: application/json" http://127.0.0.1:35000/data/pipeline/post/LoginHistory  -d @./accessormongo/code/pipelineQuery.json

### パイプライン指定検索-単一オブジェクト
curl --noproxy "*" -sS -L -X POST -H "Content-Type: application/json" http://127.0.0.1:35000/data/pipeline/post/User  -d @./accessormongo/code/pipelineQuerySingle.json
### パイプライン指定検索-グループ
curl --noproxy "*" -sS -L -X POST -H "Content-Type: application/json" http://127.0.0.1:35000/data/pipeline/post/LoginHistory  -d @./accessormongo/code/pipelineQueryGroup.json