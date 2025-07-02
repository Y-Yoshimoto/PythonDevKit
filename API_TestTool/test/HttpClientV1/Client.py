
# -*- coding: utf-8 -*-


# HTTPクライアントのクラス定義

# ユニットテストコードサンプル
import httpx

from abc import ABCMeta

# Clientの抽象クラス定義
class Client_ABC(metaclass=ABCMeta):
    """
    HTTPクライアントクラス。
    このクラスは、指定されたベースURLに対してHTTPリクエストを送信するためのメソッドを提供します。
    Attributes:
        baseURL (str): リクエストのベースURL。
    """
    def __init__(self, baseURL: str):
        # ベースURLを初期化
        self.baseURL: str = baseURL
        # HTTPクライアントの初期化
        # https://www.python-httpx.org/advanced/clients/
        self.client = httpx.Client(base_url=baseURL, timeout=None, follow_redirects=True)
    
    def __del__(self):
        """クライアントのリソースを解放する"""
        self.client.close()

    def get(self, path: str):
        """
        指定されたパスに対してGETリクエストを送信する。
        Args:
            path (str): リクエストのパス。
        Returns:
            httpx.Response: レスポンスオブジェクト。
        """
        return self.client.get(path)

    def getWithBody(self, path: str, body: dict):
        """
        指定されたパスに対してBodyを付けてGETリクエストを送信する。
        Args:
            path (str): リクエストのパス。
            body (dict): リクエストボディ。
        Returns:
            httpx.Response: レスポンスオブジェクト。
        """
        req = httpx.Request("GET", path, json=body)
        return self.client.send(req)

    def post(self, path: str, data: dict):
        """
        指定されたパスに対してPOSTリクエストを送信する。
        Args:
            path (str): リクエストのパス。
            data (dict): 送信するデータ。
        Returns:
            httpx.Response: レスポンスオブジェクト。
        """
        return self.client.post(path, json=data)

    def put(self, path: str, data: dict):
        """
        指定されたパスに対してPUTリクエストを送信する。
        Args:
            path (str): リクエストのパス。
            data (dict): 送信するデータ。
        Returns:
            httpx.Response: レスポンスオブジェクト。
        """
        return self.client.put(path, json=data)

    def delete(self, path: str):
        """
        指定されたパスに対してDELETEリクエストを送信する。
        Args:
            path (str): リクエストのパス。
        Returns:
            httpx.Response: レスポンスオブジェクト。
        """
        return self.client.delete(path)


# HttpClient.Client.py
class HttpClient(Client_ABC):
    """
    HTTPクライアントクラス。
    このクラスは、指定されたベースURLに対してHTTPリクエストを送信するためのメソッドを提供します。
    Attributes:
        baseURL (str): リクエストのベースURL。
    """
    def __init__(self, baseURL: str):
        super().__init__(baseURL)
