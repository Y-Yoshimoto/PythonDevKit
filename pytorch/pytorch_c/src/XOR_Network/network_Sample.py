#!/usr/bin/env python
# coding:utf-8

# PyTorch
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
# 基本ライブラリ
import os
import copy
import json
from functools import reduce

# 再現性用
# seed = 0
# torch.manual_seed(seed)
# torch.backends.cudnn.deterministic = True
# torch.backends.cudnn.benchmark = False
# torch.use_deterministic_algorithms = True


# 2入力, 1出力, 2層のニューラルネットワーク


class N_2LayerPerceptron(nn.Module):
    # ネットワーク構造
    def __init__(self, input=2, middle=6, output=1, device="cpu"):
        super(N_2LayerPerceptron, self).__init__()
        # 各層の定義
        self.fc1 = nn.Linear(input, middle)
        self.fc2 = nn.Linear(middle, output)

    # 順伝搬
    def forward(self, inData):
        # ネットワーク接続定義
        _nw = self._composition([
            self.fc1, torch.sigmoid,
            self.fc2, torch.sigmoid])
        return _nw(inData)

    # 関数合成高階関数
    def _composition(self, functions):
        def conmpose(initial_value):
            return reduce(lambda x, f: f(x), functions, initial_value)
        return conmpose

    # 推論関数
    def inference(self, inData):
        with torch.no_grad():
            return self.model(inData).round()


class Traing():
    def __init__(self, model, learning_rate=0.1):
        self.model = model
        # 損失関数: 平均二乗誤差 (Mean Squared Error, MSE)
        self.criterion = nn.MSELoss()
        # 最適化: 確率的勾配降下法 (Stochastic Gradient Descent, SGD)
        self.optimizer = optim.SGD(self.model.parameters(), lr=learning_rate)

    # 教師付き学習
    def train(self, train_data, epochs=10000):
        print('Training the model...')
        self.model.train()
        print(self.model.training)
        T_train_data = self.makeDataset(train_data['x'], train_data['t'])
        T_train_data = self._spritMiniBatch(T_train_data, 1)

        print(T_train_data.x)
        for epoch in range(1, epochs + 1, 1):
            self.optimizer.zero_grad()
            outputs = self.model(T_train_data.x)
            loss = self.criterion(outputs, T_train_data.t)
            loss.backward()
            self.optimizer.step()
            # 1000エポックごとに損失を表示
            if (epoch) % 1000 == 0:
                print(f'Epoch [{epoch}/10000], Loss: {loss.item():.4f}')
        # 最終損失関数値
        self.model.eval()
        print(self.model.training)
        # self.test(train_data)

    def test(self, data):
        print(model.training)
        data = self.makeDataset(data['x'], data['t'])
        with torch.no_grad():
            predicted = self.model(data.x).round()
            print(f'Predicted outputs:\n{predicted}')
            print(f'Actual outputs:\n{data['out']}')

    # データセット作成メソッド
    @classmethod
    def makeDataset(cls, x: list, t: list):
        return torch.utils.data.TensorDataset(
            torch.tensor(x, dtype=torch.float32),
            torch.tensor(t, dtype=torch.int64)
        )

    def _spritMiniBatch(self, data, batch_size, shuffle=False):
        return torch.utils.data.DataLoader(data, batch_size=batch_size, shuffle=shuffle)


# Initialize the model, loss function, and optimizer
model = N_2LayerPerceptron()

# XOR dataset
trainX = [[0, 0], [0, 1], [1, 0], [1, 1]]
trainT = [[0], [1], [1], [0]]

TraingInstance = Traing(model)
TraingInstance.train(train_data={'x': trainX, 't': trainT}, epochs=10000)
TraingInstance.test(train_data={'x': trainX, 't': trainT})
# 推論
print(model(torch.tensor([0, 0]).float()).round())

"""
#  学習ループ
for epoch in range(10000):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, Y)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 1000 == 0:
        print(f'Epoch [{epoch + 1}/10000], Loss: {loss.item():.4f}')

# Test the model
with torch.no_grad():
    predicted = model(X).round()
    print(f'Predicted outputs:\n{predicted}')
    print(f'Actual outputs:\n{Y}')
"""
