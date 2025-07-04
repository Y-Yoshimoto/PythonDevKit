# -*- coding: utf-8 -*-
# ユニットテストコードサンプル
# https://docs.pytest.org/en/stable/getting-started.html
from HttpClient.Client import HttpClient

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestClass:
    def __init__(self, baseURL: str ):
        self.requestClient = HttpClient(baseURL)


    def test_snnip(self):
        response = self.requestClient.post("", {"id": 4, "name": "test"})
        print(response.text, flush=True)
        assert response.json()["id"] == 4
        assert response.status_code == 200

    # GETリクエスト
    def test_get(self):
        response = self.requestClient.get("4")
        print(response.text, flush=True)
        assert response.json()["id"] == 4
        assert response.status_code == 200

    # POSTリクエスト
    def test_post(self):
        response = self.requestClient.post("", {"id": 4, "name": "test"})
        print(response.text, flush=True)
        assert response.json()["id"] == 4
        assert response.status_code == 200

    # PUTリクエスト
    def test_put(self):
        response = self.requestClient.put("4", {"id": 4,"name": "test_updated"})
        print(response.text, flush=True)
        assert response.json()["name"] == "test_updated"
        assert response.status_code == 200

    # DELETEリクエスト
    def test_delete(self):
        response = self.requestClient.delete("4")
        print(response.text, flush=True)
        assert response.status_code == 200


def test_request(caplog, request):
    """
    ユニットテストの実行 \n
    クラスインスタンス経由の場合はテスト関数を使用する
    """
    caplog.set_level(logging.INFO)
    logger.info("ユニットテストを実行します。")

    # 環境変数の表示
    for key, value in request.config.env.items():
        print(f"{key}={value}", flush=True)

    test_instance = TestClass(baseURL="http://127.0.0.1:8000/RestSample")
    test_instance.test_snnip()
    # test_instance.test_get()
    # test_instance.test_post()
    # test_instance.test_put()
    # test_instance.test_delete()


# スニペット実行用
if __name__ == "__main__":
    test_instance = TestClass(baseURL="http://127.0.0.1:8000/RestSample")
    test_instance.test_snnip()

"""
Try-exceptサンプル
try:
    with httpx.Client() as client:
        response = client.get(url)
        return response
except httpx.ConnectError as exc:
    raise RuntimeError(f"接続エラーが発生しました: {exc}") from exc
"""

