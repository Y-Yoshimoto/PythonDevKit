#!/usr/bin/env python
# coding:utf-8

# PyTorch
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
# 基本ライブラリ
import os, copy, json

# 再現性用
# seed = 0
# torch.manual_seed(seed)
# torch.backends.cudnn.deterministic = True
# torch.backends.cudnn.benchmark = False
# torch.use_deterministic_algorithms = True

# XOR dataset
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
Y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# XOR用の2入力, 1出力, 2層のニューラルネットワーク
class XORNetwork(nn.Module):
    def __init__(self, device="cpu"):
        super(XORNetwork, self).__init__()
        self.fc1 = nn.Linear(2, 6)
        self.fc2 = nn.Linear(6, 1)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Initialize the model, loss function, and optimizer
model = XORNetwork()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

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