"""
User service for business logic operations.
"""

from typing import List, Optional
from .models import User, UserCreate, UserUpdate
from .repository import UserRepository


class UserService:
    """
    ユーザービジネスロジック層
    """

    def __init__(self, repository: UserRepository = None):
        """
        サービスの初期化

        Args:
            repository (UserRepository): ユーザーリポジトリ
        """
        self.repository = repository or UserRepository()

    def create_user(self, user_data: UserCreate) -> tuple[User, str]:
        """
        新しいユーザーを作成

        Args:
            user_data (UserCreate): 作成するユーザーのデータ

        Returns:
            tuple[User, str]: (作成されたユーザー, エラーメッセージ)
        """
        # バリデーション
        if self.repository.exists_username(user_data.username):
            return None, "ユーザー名が既に存在します"
        
        if self.repository.exists_email(user_data.email):
            return None, "メールアドレスが既に存在します"

        # ユーザー名とメールアドレスの基本的なバリデーション
        if len(user_data.username) < 3:
            return None, "ユーザー名は3文字以上である必要があります"
        
        if len(user_data.username) > 50:
            return None, "ユーザー名は50文字以下である必要があります"

        # ユーザー作成
        user = self.repository.create(user_data)
        return user, ""

    def get_user(self, user_id: int) -> Optional[User]:
        """
        ユーザーIDでユーザーを取得

        Args:
            user_id (int): ユーザーID

        Returns:
            Optional[User]: 見つかったユーザー
        """
        return self.repository.get_by_id(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        """
        ユーザー名でユーザーを取得

        Args:
            username (str): ユーザー名

        Returns:
            Optional[User]: 見つかったユーザー
        """
        return self.repository.get_by_username(username)

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        メールアドレスでユーザーを取得

        Args:
            email (str): メールアドレス

        Returns:
            Optional[User]: 見つかったユーザー
        """
        return self.repository.get_by_email(email)

    def get_all_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """
        全ユーザーを取得

        Args:
            skip (int): スキップする件数
            limit (int): 最大取得件数

        Returns:
            List[User]: ユーザーのリスト
        """
        return self.repository.get_all(skip, limit)

    def update_user(self, user_id: int, user_data: UserUpdate) -> tuple[Optional[User], str]:
        """
        ユーザー情報を更新

        Args:
            user_id (int): 更新するユーザーのID
            user_data (UserUpdate): 更新データ

        Returns:
            tuple[Optional[User], str]: (更新されたユーザー, エラーメッセージ)
        """
        # 存在チェック
        existing_user = self.repository.get_by_id(user_id)
        if not existing_user:
            return None, "ユーザーが見つかりません"

        # ユーザー名の重複チェック
        if user_data.username and user_data.username != existing_user.username:
            if self.repository.exists_username(user_data.username):
                return None, "ユーザー名が既に存在します"
            
            if len(user_data.username) < 3:
                return None, "ユーザー名は3文字以上である必要があります"
            
            if len(user_data.username) > 50:
                return None, "ユーザー名は50文字以下である必要があります"

        # メールアドレスの重複チェック
        if user_data.email and user_data.email != existing_user.email:
            if self.repository.exists_email(user_data.email):
                return None, "メールアドレスが既に存在します"

        # 更新実行
        updated_user = self.repository.update(user_id, user_data)
        return updated_user, ""

    def delete_user(self, user_id: int) -> tuple[bool, str]:
        """
        ユーザーを削除

        Args:
            user_id (int): 削除するユーザーのID

        Returns:
            tuple[bool, str]: (削除成功フラグ, エラーメッセージ)
        """
        # 存在チェック
        if not self.repository.get_by_id(user_id):
            return False, "ユーザーが見つかりません"

        # 削除実行
        success = self.repository.delete(user_id)
        return success, ""

    def activate_user(self, user_id: int) -> tuple[Optional[User], str]:
        """
        ユーザーをアクティブ化

        Args:
            user_id (int): ユーザーID

        Returns:
            tuple[Optional[User], str]: (更新されたユーザー, エラーメッセージ)
        """
        update_data = UserUpdate(is_active=True)
        return self.update_user(user_id, update_data)

    def deactivate_user(self, user_id: int) -> tuple[Optional[User], str]:
        """
        ユーザーを非アクティブ化

        Args:
            user_id (int): ユーザーID

        Returns:
            tuple[Optional[User], str]: (更新されたユーザー, エラーメッセージ)
        """
        update_data = UserUpdate(is_active=False)
        return self.update_user(user_id, update_data)

    def get_active_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """
        アクティブなユーザーのみを取得

        Args:
            skip (int): スキップする件数
            limit (int): 最大取得件数

        Returns:
            List[User]: アクティブなユーザーのリスト
        """
        all_users = self.repository.get_all(0, 1000)  # 全ユーザーを取得
        active_users = [user for user in all_users if user.is_active]
        return active_users[skip:skip + limit]

    def get_user_count(self) -> int:
        """
        総ユーザー数を取得

        Returns:
            int: ユーザー数
        """
        return self.repository.count()

    def search_users(self, query: str, skip: int = 0, limit: int = 100) -> List[User]:
        """
        ユーザーを検索（ユーザー名または氏名で部分一致）

        Args:
            query (str): 検索クエリ
            skip (int): スキップする件数
            limit (int): 最大取得件数

        Returns:
            List[User]: 検索にマッチしたユーザーのリスト
        """
        all_users = self.repository.get_all(0, 1000)  # 全ユーザーを取得
        query_lower = query.lower()
        
        matching_users = []
        for user in all_users:
            if (query_lower in user.username.lower() or 
                (user.full_name and query_lower in user.full_name.lower())):
                matching_users.append(user)
        
        return matching_users[skip:skip + limit]
