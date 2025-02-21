import torch, torchvision
print(torch.__version__, torch.cuda.is_available())

import torch
#assert torch.__version__.startswith("1.7")

# Some basic setup:
# Setup detectron2 logger
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import matplotlib.pyplot as plt
import os, json, cv2, random

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

# 画像を保存するディレクトリを作成
dirname_picture = "./pictures/"
os.makedirs(dirname_picture, exist_ok=True)

# 画像表示用の関数を定義
def cv2_imshow(img):
    plt.figure(figsize=(8, 8))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()