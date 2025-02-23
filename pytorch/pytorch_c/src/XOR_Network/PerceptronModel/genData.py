import numpy as np


def quadrant_classification(x, y):
    # 第1,3象限には1, 第2,4象限には0, 境界値は0を返す関数
    c = x * y
    return 0 if c == 0 else 1 if c > 0 else 0


def gen_random(num, seed=None):
    # 2行1列の乱数データを生成
    if seed is not None:
        np.random.seed(seed)
    random_data = 2 * np.random.rand(num, 2) - 1
    return random_data, generate_classification_tensor(random_data)


def gen_ToData(XYData):
    # 2行1列の乱数データを生成
    np_XYData = np.array(XYData)
    return np_XYData, list(generate_classification_tensor(np_XYData))


def generate_classification_tensor(data):
    # データを受け取って、それぞれの象限に対応するクラスを生成して返す関数
    classifications = [[quadrant_classification(x, y)] for x, y in data]
    return classifications


def main():
    np.set_printoptions(precision=5)  # 表示桁数の設定
    """
    x, t = gen_random(10, 0)
    print(x)
    print(t)

    x, t = gen_ToData([[-1, -1], [-1, 1], [1, -1], [1, 1]])
    print(x)
    print(t)
    """
    interval = 10
    test_input = [[x / interval, y / interval]
                  for x in range(-interval, interval + 1) for y in range(-interval, interval + 1)]
    print(test_input)

    x, t = gen_ToData(test_input)
    print(t)


if __name__ == "__main__":
    main()
