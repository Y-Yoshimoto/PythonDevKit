# PyTorch
import torch
import torch.nn as nn
# 基本ライブラリ
from functools import reduce
import logging

# 設定
torch.set_printoptions(edgeitems=1000)
# 乱数固定
# seed = 0
# torch.manual_seed(seed)
# torch.backends.cudnn.deterministic = True
# torch.backends.cudnn.benchmark = False
# torch.use_deterministic_algorithms = True


class N_2LayerPerceptron(nn.Module):
    # 2入力, 1出力, 2層のニューラルネットワーク
    # ネットワーク構造
    def __init__(self, input=2, middle=3, output=1):
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        super(N_2LayerPerceptron, self).__init__()
        # 各層の定義
        self.fc1 = nn.Linear(input, middle)
        self.fc2 = nn.Linear(middle, output)

    def forward(self, t_inData: torch.Tensor):
        # 順伝搬 ネットワーク定義
        _nw = self._composition([
            self.fc1, torch.sigmoid,
            self.fc2, torch.sigmoid])
        return _nw(t_inData)

    def inference(self, inData: list):
        # 推論関数
        t_inData = torch.tensor(inData, dtype=torch.float32)
        with torch.no_grad():
            # return int(self(t_inData).round()[0].item())
            return self(t_inData).round()[0].item()

    def inference_not_round(self, inData: list):
        # 推論関数
        t_inData = torch.tensor(inData, dtype=torch.float32)
        with torch.no_grad():
            return self(t_inData)[0].item()

    def _composition(self, functions):
        # 関数合成高階関数(h.g.f(x) = h(g(f(x))))
        def conmpose(initial_value):
            return reduce(lambda x, f: f(x), functions, initial_value)
        return conmpose

    def saveModel(self, path):
        # モデル保存
        torch.save(self.state_dict(), path)

    def loadModel(self, path):
        # モデル読み込み
        self.load_state_dict(torch.load(path))

    def showModel(self):
        logging.info('Model Info')
        logging.info(self)
