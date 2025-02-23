#!/usr/bin/env python
# coding:utf-8

# 補助ライブラリ
import genData as gd


# ネットワークモデル
from model import N_2LayerPerceptron
# 学習クラス
from traing import Traing


def network(middle=20, epoch=3000,  num_tain_datas=200, batch_size=50, learning_rate=0.1, pickup_epoch=20, exportMiddle3D=False):
    # 訓練データ定義 ---------------------------------------------
    # train_input = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    # train_output = [[0], [1], [1], [0]]
    train_input, train_output = gd.gen_random(num_tain_datas, 0)

    # 検証データ
    val_input = [[-1, -1], [-1, 1], [1, -1], [1, 1],
                 [-0.5, -0.5], [-0.5, 0.5], [0.5, -0.5], [0.5, 0.5],
                 [-0.1, -0.1], [-0.1, 0.1], [0.1, -0.1], [0.1, 0.1]]
    val_output = [[1], [0], [0], [1],
                  [1], [0], [0], [1], [1], [0], [0], [1]]
    # テストデータ(正解データ)
    interval = 40
    test_input = [[x / interval, y / interval]
                  for x in range(-interval, interval + 1) for y in range(-interval, interval + 1)]
    _, test_output = gd.gen_ToData(test_input)
    # ---------------------------------------------------------

    # テンソル変換
    train_data = Traing.makeDataset(train_input, train_output)
    val_data = Traing.makeDataset(val_input, val_output)
    test_data = Traing.makeDataset(test_input, test_output)

    # ネットワーク構成
    model = N_2LayerPerceptron(input=2, middle=middle, output=1)

    # 学習クラス生成
    TraingInstance = Traing(
        model=model, learning_rate=0.1, batch_size=min(batch_size, num_tain_datas))

    # 学習
    trainResule = TraingInstance.train(
        epochs=epoch,
        train_data=train_data,
        val_data=val_data,
        test_data=test_data,
        pickup_epoch=pickup_epoch,
        exportMiddle3D=exportMiddle3D
    )
    print(trainResule[0])

    # 評価
    # 正解率計算
    model.showModel()
    TraingInstance.eval_accuracy()
    # グラフ出力
    TraingInstance.eval_dataGraphing()
    TraingInstance.eval_trainResuleGraphing()


def main():
    network()


if __name__ == "__main__":
    main()
