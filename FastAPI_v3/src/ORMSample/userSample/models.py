"""
User models for data representation.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from dataclasses import dataclass


@dataclass
class User:
    """
    ユーザーを表すデータクラス
    """
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    full_name: Optional[str] = None
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        """初期化後の処理"""
        if self.created_at is None:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """辞書形式に変換"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """辞書からUserオブジェクトを作成"""
        user = cls()
        for key, value in data.items():
            if hasattr(user, key):
                if key in ["created_at", "updated_at"] and isinstance(value, str):
                    setattr(user, key, datetime.fromisoformat(value))
                else:
                    setattr(user, key, value)
        return user


class UserCreate(BaseModel):
    """
    ユーザー作成用のPydanticモデル
    """
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

    class Config:
        """設定クラス"""
        schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "full_name": "John Doe",
                "is_active": True
            }
        }


class UserUpdate(BaseModel):
    """
    ユーザー更新用のPydanticモデル
    """
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        """設定クラス"""
        schema_extra = {
            "example": {
                "username": "john_doe_updated",
                "email": "john.updated@example.com",
                "full_name": "John Doe Updated",
                "is_active": False
            }
        }


class UserResponse(BaseModel):
    """
    ユーザーレスポンス用のPydanticモデル
    """
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        """設定クラス"""
        from_attributes = True
