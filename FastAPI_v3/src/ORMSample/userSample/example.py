"""
Usage examples for the User classes.
"""

from .models import UserCreate, UserUpdate
from .service import UserService


def example_usage():
    """ユーザークラスの使用例"""
    
    # サービスインスタンスの作成
    user_service = UserService()
    
    print("=== ユーザー管理システムの使用例 ===\n")
    
    # 1. ユーザー作成
    print("1. ユーザー作成")
    user_data = UserCreate(
        username="john_doe",
        email="john@example.com",
        full_name="John Doe"
    )
    
    user, error = user_service.create_user(user_data)
    if user:
        print(f"ユーザーが作成されました: {user.username} (ID: {user.id})")
    else:
        print(f"エラー: {error}")
    
    # 2. 複数ユーザー作成
    print("\n2. 複数ユーザー作成")
    users_data = [
        UserCreate(username="alice", email="alice@example.com", full_name="Alice Smith"),
        UserCreate(username="bob", email="bob@example.com", full_name="Bob Johnson"),
        UserCreate(username="charlie", email="charlie@example.com", full_name="Charlie Brown")
    ]
    
    for user_data in users_data:
        user, error = user_service.create_user(user_data)
        if user:
            print(f"ユーザーが作成されました: {user.username} (ID: {user.id})")
        else:
            print(f"エラー: {error}")
    
    # 3. ユーザー取得
    print("\n3. ユーザー取得")
    user = user_service.get_user(1)
    if user:
        print(f"ユーザー情報: {user.to_dict()}")
    
    # 4. ユーザー名での検索
    print("\n4. ユーザー名での検索")
    user = user_service.get_user_by_username("alice")
    if user:
        print(f"見つかったユーザー: {user.username} - {user.full_name}")
    
    # 5. 全ユーザー取得
    print("\n5. 全ユーザー取得")
    all_users = user_service.get_all_users()
    print(f"総ユーザー数: {len(all_users)}")
    for user in all_users:
        print(f"  - {user.username} ({user.email}) - アクティブ: {user.is_active}")
    
    # 6. ユーザー更新
    print("\n6. ユーザー更新")
    update_data = UserUpdate(
        full_name="John Doe Updated",
        email="john.updated@example.com"
    )
    updated_user, error = user_service.update_user(1, update_data)
    if updated_user:
        print(f"ユーザーが更新されました: {updated_user.to_dict()}")
    else:
        print(f"エラー: {error}")
    
    # 7. ユーザー検索
    print("\n7. ユーザー検索")
    search_results = user_service.search_users("Alice")
    print(f"検索結果 ('Alice'): {len(search_results)}件")
    for user in search_results:
        print(f"  - {user.username}: {user.full_name}")
    
    # 8. ユーザー非アクティブ化
    print("\n8. ユーザー非アクティブ化")
    user, error = user_service.deactivate_user(2)
    if user:
        print(f"ユーザー {user.username} を非アクティブ化しました")
    
    # 9. アクティブユーザーのみ取得
    print("\n9. アクティブユーザーのみ取得")
    active_users = user_service.get_active_users()
    print(f"アクティブユーザー数: {len(active_users)}")
    for user in active_users:
        print(f"  - {user.username} (アクティブ: {user.is_active})")
    
    # 10. ユーザー削除
    print("\n10. ユーザー削除")
    success, error = user_service.delete_user(4)
    if success:
        print("ユーザーが削除されました")
    else:
        print(f"エラー: {error}")
    
    # 11. 最終的なユーザー数確認
    print(f"\n最終的なユーザー数: {user_service.get_user_count()}")
    
    print("\n=== 使用例終了 ===")


if __name__ == "__main__":
    example_usage()
