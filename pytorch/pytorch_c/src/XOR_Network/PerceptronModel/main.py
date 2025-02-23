from network import network


def main():
    network(middle=5,  # 中間層のニューロン数
            epoch=10000,  # エポック数
            num_tain_datas=100,  # 訓練データ数
            batch_size=20,  # バッチサイズ
            learning_rate=0.1,  # 学習率
            pickup_epoch=20,  # 学習経過の表示数
            exportMiddle3D=False  # 中間3Dグラフ出力
            )


if __name__ == "__main__":
    main()
