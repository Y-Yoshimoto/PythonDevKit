
# -*- coding: utf-8 -*-
# ユニットテストコードサンプル
import httpx
# HTTPクライアントのクラス定義

class Client:
    def __init__(self, baseURL: str):
        self.baseURL: str = baseURL
    
    def generateURL(self, path: str):
        """指定されたパスを基に完全なURLを生成する"""
        # return f"{self.baseURL}/{path}" if path else self.baseURL
        return f"{self.baseURL}/{path}"

    # GETリクエスト
    def get(self, path: str):
        url = self.generateURL(path)
        with httpx.Client() as client:
            return client.get(url)
        
    # POSTリクエスト
    def post(self, path: str, data: dict):
        url = self.generateURL(path)
        with httpx.Client() as client:
            return client.post(url, json=data)
        
    # PUTリクエスト
    def put(self, path: str, data: dict):
        url = self.generateURL(path)
        with httpx.Client() as client:
            return client.put(url, json=data)
    
    # DELETEリクエスト
    def delete(self, path: str):
        url = self.generateURL(path)
        with httpx.Client() as client:
            return client.delete(url)