# ユーザー管理システム

このディレクトリには、ユーザーを扱うPythonクラスが含まれています。ディレクトリを分けて管理された、モジュラーな設計になっています。

## ディレクトリ構造

```
user/
├── __init__.py          # パッケージ初期化ファイル
├── models.py            # ユーザーモデルクラス
├── repository.py        # データアクセス層
├── service.py           # ビジネスロジック層
├── api.py              # FastAPI統合用エンドポイント
├── example.py          # 使用例
└── README.md           # このファイル
```

## 主要なクラス

### 1. User (models.py)
- メインのユーザーデータクラス
- 基本的なユーザー情報（ID、ユーザー名、メール、フルネーム等）
- 作成日時、更新日時の自動管理
- 辞書への変換メソッド

### 2. UserCreate, UserUpdate (models.py)
- Pydanticモデルでバリデーション機能付き
- API入力用のデータクラス
- メールアドレスの形式チェック機能

### 3. UserRepository (repository.py)
- データアクセス層
- CRUD操作の実装
- メモリ上での簡単な実装（実際のプロジェクトではDB接続）

### 4. UserService (service.py)
- ビジネスロジック層
- バリデーション処理
- エラーハンドリング
- 高レベルな操作の提供

### 5. FastAPI統合 (api.py)
- RESTful APIエンドポイント
- HTTPエラーハンドリング
- クエリパラメータ対応

## 使用方法

### 基本的な使用例

```python
from user import UserService, UserCreate

# サービスインスタンスの作成
user_service = UserService()

# ユーザー作成
user_data = UserCreate(
    username="john_doe",
    email="john@example.com",
    full_name="John Doe"
)

user, error = user_service.create_user(user_data)
if user:
    print(f"ユーザーが作成されました: {user.username}")
else:
    print(f"エラー: {error}")

# ユーザー取得
user = user_service.get_user(1)
if user:
    print(user.to_dict())
```

### FastAPIでの使用

```python
from fastapi import FastAPI
from user.api import user_router

app = FastAPI()
app.include_router(user_router)

# サーバー起動後、以下のエンドポイントが利用可能：
# POST /users/           - ユーザー作成
# GET /users/            - ユーザー一覧取得
# GET /users/{id}        - 特定ユーザー取得
# PUT /users/{id}        - ユーザー更新
# DELETE /users/{id}     - ユーザー削除
# GET /users/search      - ユーザー検索
```

## 実行例

```bash
# 使用例の実行
cd /app/src/ORMSample
python -c "from user.example import example_usage; example_usage()"

# または
python test_user.py
```

## 機能

- ✅ ユーザーのCRUD操作
- ✅ バリデーション（ユーザー名重複チェック、メール形式チェック等）
- ✅ 検索機能（ユーザー名、フルネームでの部分一致）
- ✅ アクティブ/非アクティブ管理
- ✅ ページネーション対応
- ✅ FastAPI統合
- ✅ エラーハンドリング
- ✅ レスポンス用データモデル

## 今後の拡張案

- データベース接続（SQLAlchemy、SQLModel等）
- 認証・認可機能
- パスワードハッシュ化
- ロール管理
- ユーザーグループ機能
- 監査ログ
- キャッシュ機能

## 依存関係

- `fastapi` - Web フレームワーク
- `pydantic` - データバリデーション
- `email-validator` - メールアドレス検証
