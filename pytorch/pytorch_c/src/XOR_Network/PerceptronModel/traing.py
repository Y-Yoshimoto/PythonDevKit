#!/usr/bin/env python
# coding:utf-8

# PyTorch
import torch
import torch.nn as nn
import torch.optim as optim
# 補助ライブラリ
import genGraph as gg


class Traing():
    # 学習クラス
    def __init__(self, model, learning_rate=0.1, batch_size=2):
        self.model = model
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        # 学習パラメータ
        self.batch_size = batch_size
        self.learning_rate = learning_rate

        # 損失関数: 平均二乗誤差 (Mean Squared Error, MSE)
        self.criterion = nn.MSELoss()
        # 最適化: 確率的勾配降下法 (Stochastic Gradient Descent, SGD)
        self.optimizer = optim.SGD(
            self.model.parameters(), lr=self.learning_rate)

    # 学習系メソッド

    def train(self, train_data, val_data, test_data, epochs=10000, pickup_epoch=20, exportMiddle3D=False):
        # 教師付き学習
        print('Training the model...')
        self.model.train()   # 学習モード切り替え
        # 学習データ登録
        self.train_data = train_data
        self.val_data = val_data
        self.test_data = test_data
        self.exportMiddle3D = exportMiddle3D
        # 学習
        self.trainResule = [info
                            for info in self._traingGeneter(max_epoch=epochs, pickup_epoch=pickup_epoch)]
        # 最終損失関数値
        self.model.eval()    # 評価モード切り替え
        return self.trainResule

    def _traingGeneter(self, max_epoch=10000, pickup_epoch=20):
        # 学習ジェネレーター
        each = max_epoch / pickup_epoch
        for epoch in range(1, max_epoch + 1):
            self._oneEpoch(epoch)
            if epoch % each == 0:
                yield self._exportInfo(epoch)

    def _exportInfo(self, epoch):
        # 学習情報出力
        train_info = self.calc_accuracy(self.train_data)
        val_info = self.calc_accuracy(self.val_data)
        test_info = self.calc_accuracy(self.test_data)
        print(
            f'Epoch [{epoch}], Loss_train: {train_info["loss"]:.4f}, Loss: {val_info["loss"]:.4f}, Accuracy: {val_info["accuracy"]:.4f}')
        if (self.exportMiddle3D):
            self.middle_dataGraphing(
                self.test_data, f'Result_testMiddle.jpeg', f'Epoch_{epoch}')
        return {'epoch': epoch, 'train': train_info, 'val': val_info, 'test': test_info}

    def _oneEpoch(self, epoch):
        # 1エポック分の学習
        baches = self._spritMiniBatch(self.train_data, self.batch_size, True)
        lossList = [self._oneBach(batch) for batch in baches]
        return sum(lossList)

    def _oneBach(self, batch):
        # 1バッチ分の学習
        x, t = batch[0].to(self.device), batch[1].to(self.device)
        self.optimizer.zero_grad()
        loss = self.criterion(self.model(x), t)
        loss.backward()
        self.optimizer.step()
        return loss

    def calc_accuracy(self, data):
        # 正解率計算
        baches = self._spritMiniBatch(data, self.batch_size)
        with torch.no_grad():
            reList = [self._oneBach_accuracy(batch) for batch in baches]
        return {'loss': sum([re['p_loss'] for re in reList])/len(data),
                'accuracy': sum([re['p_accuracy'] for re in reList])/len(data)}

    def _oneBach_accuracy(self, batch):
        # 1バッチ分の損出正解率計算
        x, t = batch[0].to(self.device), batch[1].to(self.device)
        y = self.model(x)
        loss, ans = self.criterion(y, t), torch.sum(y.round() == t)
        return {'p_loss': loss.item(), 'p_accuracy': ans.item()}

    def middle_dataGraphing(self, data, filename, title):
        # 中間結果グラフ出力
        X = [d[0][0].item() for d in data]
        Y = [d[0][1].item() for d in data]
        # Z = [self.model.inference(d[0].tolist()) for d in data]
        Z = [self.model.inference_not_round(d[0].tolist()) for d in data]
        gg.plot_3d_graph(X, Y, Z, filename, title)

    # 評価系メソッド

    def eval_accuracy(self):
        # 最終評価値分析
        print('Calculating accuracy...')
        self.model.eval()
        train_info = self.calc_accuracy(self.train_data)
        val_info = self.calc_accuracy(self.val_data)
        test_info = self.calc_accuracy(self.test_data)
        print(
            f'Accuracy Train:     {train_info["accuracy"]:.4f} / Loss: {train_info["loss"]:.4f}')
        print(
            f'Accuracy Vlidation: {val_info["accuracy"]:.4f} / Loss: {val_info["loss"]:.4f}')
        print(
            f'Accuracy Test:      {test_info["accuracy"]:.4f} / Loss: {test_info["loss"]:.4f}')

        return {'train': train_info, 'val': val_info, 'test': test_info}

    def eval_dataGraphing(self):
        self._graphic(self.train_data, 'Result_train.jpeg', 'Train')
        self._graphic(self.val_data, 'Result_vlidation.jpeg', 'Vlidation')
        self._graphic(self.test_data, 'Result_test.jpeg', 'Test')

    def _graphic(self, data, filename, title):
        # 推論/正解のセットグラフ描画
        X = [d[0][0].item() for d in data]
        Y = [d[0][1].item() for d in data]
        # Z = [self.model.inference(d[0].tolist()) for d in data]
        Z = [self.model.inference_not_round(d[0].tolist()) for d in data]
        T = [d[1][0].item() for d in data]
        gg.plot_3d_graph2(X, Y, Z, T, filename,
                          f'{title}_inference', f'{title}_Answer')

    def eval_trainResuleGraphing(self):
        # 学習結果グラフ出力(損出関数と正解率)
        gg.plot_2d_Result_lossAndAccuracyGraph(
            self.trainResule, filename='Result_lossAndAccuracy.jpeg', title='Loss and Accuracy')

    @classmethod
    def makeDataset(cls, x: list, t: list):
        # データセット作成メソッド
        return torch.utils.data.TensorDataset(
            torch.tensor(x, dtype=torch.float32),
            torch.tensor(t, dtype=torch.float32)
        )

    @classmethod
    def _spritMiniBatch(cls, dataset, batch_size, shuffle=False):
        # ミニバッチ分割
        return torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
