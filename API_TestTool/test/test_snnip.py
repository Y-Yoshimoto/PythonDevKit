# -*- coding: utf-8 -*-
# ユニットテストコードサンプル
# https://docs.pytest.org/en/stable/getting-started.html
from HttpClient.Client import HttpClient
import pytest
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="class")
def re_client():
    print("セットアップを実行します。", flush=True)
    requestClient = HttpClient(domain="127.0.0.1:8000", base_path="/RestSample")
    yield requestClient

class TestClass:

    def test_snnip(self, re_client):
        response = re_client.request("POST", "", {}, {"id": 4, "name": "test"})
        print(response.text, flush=True)
        assert response.json()["id"] == 4
        assert response.status_code == 200

    # GETリクエスト
    def test_get(self, re_client):
        response = re_client.request("GET", "4")
        print(response.text, flush=True)
        assert response.json()["id"] == 4
        assert response.status_code == 200

    # POSTリクエスト
    def test_post(self, re_client):
        response = re_client.request("POST", "", {}, {"id": 4, "name": "test"})
        print(response.text, flush=True)
        assert response.json()["id"] == 4
        assert response.status_code == 200

    # PUTリクエスト
    def test_put(self, re_client):
        response = re_client.request("PUT", "4", {}, {"id": 4,"name": "test_updated"})
        print(response.text, flush=True)
        assert response.json()["name"] == "test_updated"
        assert response.status_code == 200

    # DELETEリクエスト
    def test_delete(self, re_client):
        response = re_client.request("DELETE", "4")
        print(response.text, flush=True)
        assert response.status_code == 200

@pytest.mark.skip(reason="スニペット実行用")
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
    with httpx.Client() as re_client:
        response = re_client.get(url)
        return response
except httpx.ConnectError as exc:
    raise RuntimeError(f"接続エラーが発生しました: {exc}") from exc
"""

