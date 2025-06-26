"""
User API endpoints for FastAPI integration.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List

from .models import UserCreate, UserUpdate, UserResponse
from .service import UserService

# ルーターの作成
user_router = APIRouter(prefix="/users", tags=["users"])

# サービスインスタンス（通常は依存性注入を使用）
user_service = UserService()


@user_router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate):
    """
    新しいユーザーを作成
    """
    user, error = user_service.create_user(user_data)
    if error:
        raise HTTPException(status_code=400, detail=error)
    
    return UserResponse(**user.to_dict())


@user_router.get("/", response_model=List[UserResponse])
async def get_users(
    skip: int = Query(0, ge=0, description="スキップする件数"),
    limit: int = Query(100, ge=1, le=1000, description="最大取得件数"),
    active_only: bool = Query(False, description="アクティブユーザーのみ取得")
):
    """
    ユーザー一覧を取得
    """
    if active_only:
        users = user_service.get_active_users(skip=skip, limit=limit)
    else:
        users = user_service.get_all_users(skip=skip, limit=limit)
    
    return [UserResponse(**user.to_dict()) for user in users]


@user_router.get("/search", response_model=List[UserResponse])
async def search_users(
    q: str = Query(..., min_length=1, description="検索クエリ"),
    skip: int = Query(0, ge=0, description="スキップする件数"),
    limit: int = Query(100, ge=1, le=1000, description="最大取得件数")
):
    """
    ユーザーを検索
    """
    users = user_service.search_users(q, skip=skip, limit=limit)
    return [UserResponse(**user.to_dict()) for user in users]


@user_router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """
    指定されたIDのユーザーを取得
    """
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    
    return UserResponse(**user.to_dict())


@user_router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserUpdate):
    """
    ユーザー情報を更新
    """
    user, error = user_service.update_user(user_id, user_data)
    if error:
        if "見つかりません" in error:
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)
    
    return UserResponse(**user.to_dict())


@user_router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    """
    ユーザーを削除
    """
    success, error = user_service.delete_user(user_id)
    if not success:
        if "見つかりません" in error:
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)


@user_router.post("/{user_id}/activate", response_model=UserResponse)
async def activate_user(user_id: int):
    """
    ユーザーをアクティブ化
    """
    user, error = user_service.activate_user(user_id)
    if error:
        if "見つかりません" in error:
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)
    
    return UserResponse(**user.to_dict())


@user_router.post("/{user_id}/deactivate", response_model=UserResponse)
async def deactivate_user(user_id: int):
    """
    ユーザーを非アクティブ化
    """
    user, error = user_service.deactivate_user(user_id)
    if error:
        if "見つかりません" in error:
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)
    
    return UserResponse(**user.to_dict())


@user_router.get("/username/{username}", response_model=UserResponse)
async def get_user_by_username(username: str):
    """
    ユーザー名でユーザーを取得
    """
    user = user_service.get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    
    return UserResponse(**user.to_dict())


@user_router.get("/stats/count")
async def get_user_count():
    """
    総ユーザー数を取得
    """
    count = user_service.get_user_count()
    return {"total_users": count}
