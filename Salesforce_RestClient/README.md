# Python Dev

Pythonのコード実行環境用コンテナ  

## コンテナ

- python  
  Python実行環境

## サンプルコード

## 付随ファイル

- Dockerfile  
Dockerファイル
- docker-compose.yaml  
Docker composeのマニフェストファイル
- .env  
環境変数定義ファイル .env.protをコピーして作成
- requirements.txt  
pipでインストールするライブラリーの定義ファイル

## srcディレクトリについて

python_dev/srcディレクトリは、コンテナ内の/usr/srcにマウント


## Salesforce上の設定変更内容(ハンズオン組織向け)
1. ユーザーパスワードの再発行とドメインの確認
  - ユーザー一覧からパスワードのリセットを行い受信したメールからパスワードをリセットする。
  - 必要であればメールアドレスの変更を事前に行う。
  - ユーザーの設定でAPIの有効化をONにする。
  - 設定で「私のドメイン」で検索しドメインの確認を行う。
  - 参考: [Trailhead Playground のユーザー名とパスワードの取得](https://trailhead.salesforce.com/ja/content/learn/modules/trailhead_playground_management/get-your-trailhead-playground-username-and-password)
2. 接続に使用する証明書と秘密鍵を生成
  - 証明書と秘密鍵を生成するためのコマンドを実行する。証明書の質問の答えのうち、パスワードは設定が必要。
  ```bash
  which openssl
  cd certificate
  openssl genpkey -des3 -algorithm RSA -pass pass:SomePassword -out sf_jwt_certificatepass.pass.key -pkeyopt rsa_keygen_bits:2048
  openssl rsa -passin pass:SomePassword -in sf_jwt_certificatepass.pass.key -out sf_jwt_certificate.key
  rm sf_jwt_certificatepass.pass.key
  openssl req -new -key sf_jwt_certificate.key -out sf_jwt_certificate.csr
  openssl x509 -req -sha256 -days 365 -in sf_jwt_certificate.csr -signkey sf_jwt_certificate.key -out sf_jwt_certificate.crt
  ls -al
  ```
  - 参考: [非公開鍵と自己署名デジタル証明書の作成](https://developer.salesforce.com/docs/atlas.ja-jp.252.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm)
3. 外部アプリケーションの有効化
  - 外部クライアントアプリケーション設定  
  "REST API を使用した外部クライアントアプリケーションのコンシューマーの秘密へのアクセスを許可"を有効化
  - 接続アプリケーションの作成を許可  
   作成を許可を有効化