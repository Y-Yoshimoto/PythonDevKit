# -*- coding: utf-8 -*-
# ユニットテストコードサンプル
# https://docs.pytest.org/en/stable/getting-started.html
import pytest
import pytest_check as check
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestClass:

    def test_runtime(self):
        x = 1 + 1
        check.equal(x, 2, "計算結果が一致しません")


# スニペット実行用
if __name__ == "__main__":
    test_instance = TestClass()
    test_instance.test_runtime()
