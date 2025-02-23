# optunaを使ってハイパーパラメータを最適化する
import logging
import optuna
from PerceptronModel.network import network

# 最適化対象の関数


def objective(trial):
    # 探索するパラメータの範囲を指定
    middle = trial.suggest_int('middle', 2, 10)
    num_tain_datas = trial.suggest_int('num_tain_datas', 10, 200)
    batch_size = trial.suggest_int('batch_size', 10, 100)
    learning_rate = trial.suggest_float('learning_rate', 0.01, 0.5)

    resule = network(middle=middle,  # 中間層のニューロン数
                     epoch=4000,  # エポック数
                     num_tain_datas=num_tain_datas,  # 訓練データ数
                     batch_size=batch_size,  # バッチサイズ
                     learning_rate=learning_rate,  # 学習率
                     pickup_epoch=1,  # 学習経過の表示数
                     exportGraph=False  # 中間3Dグラフ出力
                     )
    return resule['val']['loss']


def main():
    # 探索設定
    study = optuna.create_study()
    study.optimize(objective, n_trials=3)
    # 最適解
    study.best_params
    # 結果表示
    print("Best trial:")
    print(study.best_params)
