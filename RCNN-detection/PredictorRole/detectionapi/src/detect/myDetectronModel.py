#!/usr/bin/env python
# coding:utf-8
import os
import cv2
import numpy as np

# Base64/zlib
import base64
import zlib

## ログ
import logging
from contextlib import redirect_stdout, redirect_stderr

# detectron2
with redirect_stderr(open(os.devnull, 'w')):
    from detectron2 import model_zoo
    from detectron2.engine import DefaultPredictor, DefaultTrainer
    from detectron2.config import get_cfg
    from detectron2.utils.visualizer import Visualizer
    from detectron2.data import MetadataCatalog, DatasetCatalog
    from detectron2.data.datasets import register_coco_instances



class BaseModel(object):
    def __init__ (self, device):
        # ログ設定
        self.logger = logging.getLogger(__name__)
        self.logger.info(f'Init Model: {__name__}')
        # Detectron2コンフィグの読み込み
        self.cfg = get_cfg() 
        # デバイス設定
        self.cfg.MODEL.DEVICE = device

    def __del__(self):
        self.logger.info(f'Del Model: {__name__}')
        
    def ExecInference_OutputImage(self,imageFilePathName: str, OutputFilePathNam: str):
        """推論実行_画像を出力
            Args:
                imageFilePathName: 推論を行う画像のパス/ファイル名
                OutputFilePathNam: 推論結果を出力する重畳画像のパス/ファイル名
            Return: null
        """
        print("ExecInference_OutputImage", flush=True)
        # 推論画像の読み込みと実行
        with redirect_stderr(open(os.devnull, 'w')):
            im = cv2.imread(imageFilePathName)
            outputs = self.predictor(im)
        #結果の出力
        #print(outputs["instances"].pred_classes)
        #print(outputs["instances"].pred_boxes)
        #print(outputs["instances"].sem_seg)
        v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        cv2.imwrite(OutputFilePathNam,out.get_image()[:, :, ::-1])
        
    ### 画像フォーマット変換 ##########################
    def loadLocalImage(self, fileName: str) -> bytes:
        with open(fileName, 'rb') as f:
            bImage = f.read()
        return bImage
    def saveLocalImage(self, fileName: str, bImage: bytes):
        with open(fileName, mode='wb') as f:
            f.write(bImage)
        
    def decodeCV2Image(self, bImage):
        arr = np.frombuffer(bImage, dtype=np.uint8)
        return cv2.imdecode(arr, flags=cv2.IMREAD_COLOR)
        
    def encodeBytesImage(self, cv2Image: np.ndarray):
        ret, bImage = cv2.imencode('.jpg', cv2Image, (cv2.IMWRITE_JPEG_QUALITY, 80))
        return bImage
    
    def encodeBase64zlib(self, cv2Image):
        bImage = self.encodeBytesImage(cv2Image)
        return zlib.compress(base64.b64encode(bImage))
    
    def decodeBase64zlib(self, zbase64):
        bImage = base64.b64decode(zlib.decompress(zbase64).decode())
        return self.decodeCV2Image(bImage)
    
    ### 推論処理 ##########################
    ### RAW推論結果出力
    def raw(self, bImage):
        with redirect_stderr(open(os.devnull, 'w')):
            return self.predictor(self.decodeCV2Image(bImage))
        
    ### 画像結果出力
    def inferenceImage(self, bImage):
        output = self.raw(bImage)
        cv2i = self.decodeCV2Image(bImage)
        v = Visualizer(cv2i[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1)
        cv2iP = v.draw_instance_predictions(output["instances"].to("cpu"))
        return self.encodeBytesImage(cv2iP.get_image()[:, :, ::-1])
        
    ### フォーマットデータ出力
    def inferenceData(self, bImage):
        cv2i = self.decodeCV2Image(bImage)
        # 推論実行
        with redirect_stderr(open(os.devnull, 'w')):
            result = self.predictor(cv2i)["instances"].to('cpu')
            v = Visualizer(cv2i[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1)
            cv2iPi = v.draw_instance_predictions(result).get_image()[:, :, ::-1]
            
        # 結果取り出し
        image_height, image_width = result._image_size
        bbox=result.pred_boxes.tensor.tolist()
        scores=result.scores.tolist()
        classes=result.pred_classes.tolist()
        masks=result.pred_masks.tolist()
        #mask=result.pred_masks.prod(dim=0)

        orgImage=self.encodeBase64zlib(cv2i)
        resultImage=self.encodeBase64zlib(cv2iPi)

class zooModel(BaseModel):
    def __init__ (self, type="detection", threshold=0.7, device="cpu"):
        # 基底クラスInit
        super().__init__(device)
        # Zooモデルセット(ダウンロード)
        if type == "detection":
            zooModel="COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
        elif type == "instanceSegmentation":
            zooModel="COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
        else:
            self.logger.critical(f'Select type detection or instanceSegmentation. type: {type}')
            exit
        self.cfg.merge_from_file(model_zoo.get_config_file(zooModel))
        self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(zooModel)
        # 閾値:thresholdを設定
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = threshold
        # 推論モデル作成
        self.predictor = DefaultPredictor(self.cfg)
        self.logger.info(f'Success load Model: {__name__}')

class localModel(BaseModel):
    def __init__ (self, modeldir="./TraningDataOutput/", threshold=0.7, device="cpu"):
        # 基底クラスInit
        super().__init__(device)
        # ローカルモデルの読み込み
        if modeldir[-1]!="/":
            modeldir += "/"
        # ローカルモデルの読み込み        
        self.cfg.MODEL.WEIGHTS = os.path.join(modeldir, "model_final.pth")
        #self.cfg.merge_from_file(os.path.join(modeldir, "config.yaml"))
        
        # 閾値:thresholdを設定
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = threshold
        # 推論モデル作成
        self.predictor = DefaultPredictor(self.cfg)
        self.logger.info(f'Success load Model: {__name__}')

class traingModel(zooModel, BaseModel):
    """転移学習用モデルクラス"""
    def __init__ (self, type="detection", threshold=0.7, device="cpu"):
        super().__init__(type=type, threshold=threshold, device=device)

        
    # 転移学習
    def TransferLearning(self,traningDataName:str, classesName: list, CoCoFilePathName: str, imageRootPath: str):
        # カテゴリー名称の設定
        # MetadataCatalog.get(traningDataName).thing_classes = traningMetaData
        # トレーニングデータの設定
        register_coco_instances(traningDataName, {}, CoCoFilePathName, imageRootPath)
        # 学習データの出力
        #traningDataMetaData = MetadataCatalog.get(traningDataName)
        #print(traningDataMetaData)
        #datasetDicts = DatasetCatalog.get(traningDataName)
        # #print(datasetDicts)
        # img = cv2.imread(datasetDicts[0]["file_name"])
        # visualizer = Visualizer(img[:, :, ::-1], metadata=traningDataMetaData, scale=1.0)
        # out = visualizer.draw_dataset_dict(datasetDicts[0])
        # #cv2.imwrite("./images/tmp.jpg",out.get_image()[:, :, ::-1])
        # 学習データの登録
        self.cfg.DATASETS.TRAIN = (traningDataName)
        # テストデータの登録
        self.cfg.DATASETS.TEST = () 
        # スレッド数の設定
        self.cfg.DATALOADER.NUM_WORKERS = 4
        # ステップごとのトレーニング画像枚数
        self.cfg.SOLVER.IMS_PER_BATCH = 2
        # 学習レートの設定
        self.cfg.SOLVER.BASE_LR = 0.02
        # 学数回数の設定
        self.cfg.SOLVER.MAX_ITER = (8) 
        # 画像あたりのROI(関心領域)の設定
        self.cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = (128)
        # 学習データのクラス数
        self.cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(classesName)
        # 出力先ディレクトの設定
        self.cfg.OUTPUT_DIR="./TraningDataOutput"

        print("Traning Start", flush=True)
        # 学習インスタンスの生成
        self.trainer = DefaultTrainer(self.cfg)
        # 途中経過保存設定
        self.trainer.resume_or_load(resume=False)
        # 学習の実施
        self.trainer.train()
        
        # 学習結果の設定
        print("Traning End", flush=True)       
        # 最終のモデルの重みを読み込み, カタログの再設定
        self.cfg.MODEL.WEIGHTS = os.path.join(self.cfg.OUTPUT_DIR, "model_final.pth")
        # 閾値の設定
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   
        # 推論モデルの更新
        self.predictor = DefaultPredictor(self.cfg)
        
        # 推論画像の読み込みと実行
        # im = cv2.imread("./images/input_b.jpg")
        # outputs = self.predictor(im)
        # # v = Visualizer(im[:, :, ::-1], metadata=traningDataMetaData, scale=1.0)
        # v = Visualizer(im[:, :, ::-1], metadata=MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1.0)
        # out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        # cv2.imwrite("./images/output3.jpg",out.get_image()[:, :, ::-1])