"""
User repository for data access operations.
"""

from typing import List, Optional, Dict
from .models import User, UserCreate, UserUpdate


class UserRepository:
    """
    ユーザーデータアクセス層
    メモリ上での簡単な実装（実際のプロジェクトではデータベース接続を行う）
    """

    def __init__(self):
        """リポジトリの初期化"""
        self._users: Dict[int, User] = {}
        self._next_id = 1

    def create(self, user_data: UserCreate) -> User:
        """
        新しいユーザーを作成

        Args:
            user_data (UserCreate): 作成するユーザーのデータ

        Returns:
            User: 作成されたユーザー
        """
        user = User(
            id=self._next_id,
            username=user_data.username,
            email=user_data.email,
            full_name=user_data.full_name,
            is_active=user_data.is_active
        )
        
        self._users[self._next_id] = user
        self._next_id += 1
        
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        """
        IDでユーザーを取得

        Args:
            user_id (int): ユーザーID

        Returns:
            Optional[User]: 見つかったユーザー、または None
        """
        return self._users.get(user_id)

    def get_by_username(self, username: str) -> Optional[User]:
        """
        ユーザー名でユーザーを取得

        Args:
            username (str): ユーザー名

        Returns:
            Optional[User]: 見つかったユーザー、または None
        """
        for user in self._users.values():
            if user.username == username:
                return user
        return None

    def get_by_email(self, email: str) -> Optional[User]:
        """
        メールアドレスでユーザーを取得

        Args:
            email (str): メールアドレス

        Returns:
            Optional[User]: 見つかったユーザー、または None
        """
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """
        全ユーザーを取得（ページネーション対応）

        Args:
            skip (int): スキップする件数
            limit (int): 最大取得件数

        Returns:
            List[User]: ユーザーのリスト
        """
        users_list = list(self._users.values())
        return users_list[skip:skip + limit]

    def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """
        ユーザー情報を更新

        Args:
            user_id (int): 更新するユーザーのID
            user_data (UserUpdate): 更新データ

        Returns:
            Optional[User]: 更新されたユーザー、または None
        """
        user = self._users.get(user_id)
        if not user:
            return None

        # 更新データが提供された場合のみ更新
        if user_data.username is not None:
            user.username = user_data.username
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.full_name is not None:
            user.full_name = user_data.full_name
        if user_data.is_active is not None:
            user.is_active = user_data.is_active

        # 更新時刻を更新
        from datetime import datetime
        user.updated_at = datetime.now()

        return user

    def delete(self, user_id: int) -> bool:
        """
        ユーザーを削除

        Args:
            user_id (int): 削除するユーザーのID

        Returns:
            bool: 削除が成功した場合True、そうでなければFalse
        """
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

    def exists_username(self, username: str) -> bool:
        """
        ユーザー名が既に存在するかチェック

        Args:
            username (str): チェックするユーザー名

        Returns:
            bool: 存在する場合True
        """
        return self.get_by_username(username) is not None

    def exists_email(self, email: str) -> bool:
        """
        メールアドレスが既に存在するかチェック

        Args:
            email (str): チェックするメールアドレス

        Returns:
            bool: 存在する場合True
        """
        return self.get_by_email(email) is not None

    def count(self) -> int:
        """
        総ユーザー数を取得

        Returns:
            int: ユーザー数
        """
        return len(self._users)
