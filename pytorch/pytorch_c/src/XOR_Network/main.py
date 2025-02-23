# 単一学習/モデルの実行
import logging
from PerceptronModel.network import network


def main():
    # ログ設定
    logging.basicConfig(level=logging.INFO)
    # ネットワーク実行
    resule = network(middle=5,  # 中間層のニューロン数
                     epoch=4000,  # エポック数
                     num_tain_datas=100,  # 訓練データ数
                     batch_size=20,  # バッチサイズ
                     learning_rate=0.1,  # 学習率
                     pickup_epoch=20,  # 学習経過の表示数
                     exportGraph=True  # グラフ出力
                     )
    print(resule)


if __name__ == "__main__":
    main()
