import unittest

# テスト対象の関数をインポート
import sampleFunction


# 足し算と掛け算のテストを行う
class TestAddMethods(unittest.TestCase):
    def test_add(self):
        assert sampleFunction.add(2, 3) == 5
        assert sampleFunction.add(-1, 5) == 4
        assert sampleFunction.add(0, 0) == 0
        assert sampleFunction.add(10, -10) == 0
        assert sampleFunction.add(100, 200) == 300


class TestProductMethods(unittest.TestCase):
    def test_product(self):
        assert sampleFunction.product(2, 3) == 6
        assert sampleFunction.product(-1, 5) == -5
        assert sampleFunction.product(0, 0) == 0
        assert sampleFunction.product(10, -10) == -100
        assert sampleFunction.product(100, 200) == 20000


if __name__ == "__main__":
    unittest.main()
