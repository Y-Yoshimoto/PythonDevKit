#!/usr/bin/env python
# coding:utf-8
# Some basic setup:
# Setup detectron2 logger
# import detectron2
#from detectron2.utils.logger import setup_logger
#setup_logger()

# import some common libraries
#import numpy as np
import os, json, cv2, random
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor, DefaultTrainer
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets import register_coco_instances
## データ拡張
import detectron2.data.transforms as transforms
from detectron2.data import DatasetMapper, build_detection_train_loader

class myModel:
    """転移学習用モデルクラス"""
    def __init__ (self, zooModel="COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml", 
                threshold=0.5, device="cpu"):
        print("Init", flush=True)
        # Detectron2コンフィグの読み込み
        self.cfg = get_cfg() 
        # CPUに設置
        self.cfg.MODEL.DEVICE = device

        # Zooモデルセット(ダウンロード)
        self.cfg.merge_from_file(model_zoo.get_config_file(zooModel))
        self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(zooModel)
        # 閾値:thresholdを設定
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = threshold
        
        # 推論モデル作成
        self.predictor = DefaultPredictor(self.cfg)
        
    def __del__(self):
        print("Dell")
        
    def ExecInference_OutputImage(self,imageFilePathName: str, OutputFilePathNam: str):
        """推論実行_画像を出力
            Args:
                imageFilePathName: 推論を行う画像のパス/ファイル名
                OutputFilePathNam: 推論結果を出力する重畳画像のパス/ファイル名
            Return: null
        """
        print("ExecInference_OutputImage", flush=True)
        # 推論画像の読み込みと実行
        im = cv2.imread(imageFilePathName)
        outputs = self.predictor(im)
        #結果の出力
        #print(outputs["instances"].pred_classes)
        #print(outputs["instances"].pred_boxes)
        #print(outputs["instances"].sem_seg)
        v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        cv2.imwrite(OutputFilePathNam,out.get_image()[:, :, ::-1])

    # 転移学習
    def TransferLearning(self,traningDataName:str, classesName: list, CoCoFilePathName: str, imageRootPath: str):
        # カテゴリー名称の設定
        # MetadataCatalog.get(traningDataName).thing_classes = traningMetaData
        # トレーニングデータの設定
        register_coco_instances(traningDataName, {}, CoCoFilePathName, imageRootPath)
        # 学習データの出力
        traningDataMetaData = MetadataCatalog.get(traningDataName)
        #print(traningDataMetaData)
        datasetDicts = DatasetCatalog.get(traningDataName)
        #print(datasetDicts)
        img = cv2.imread(datasetDicts[0]["file_name"])
        visualizer = Visualizer(img[:, :, ::-1], metadata=traningDataMetaData, scale=1.0)
        out = visualizer.draw_dataset_dict(datasetDicts[0])
        cv2.imwrite("./images/tmp.jpg",out.get_image()[:, :, ::-1])
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
        im = cv2.imread("./images/input_b.jpg")
        outputs = self.predictor(im)
        # v = Visualizer(im[:, :, ::-1], metadata=traningDataMetaData, scale=1.0)
        v = Visualizer(im[:, :, ::-1], metadata=MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1.0)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        cv2.imwrite("./images/output3.jpg",out.get_image()[:, :, ::-1])
        
    #  データ拡張付き転移学習
    def TransferLearningDataAugmentation(self,traningDataName:str, classesName: list, CoCoFilePathName: str, imageRootPath: str):
        train_augmentations = [
        transforms.RandomBrightness(0.5, 2),
        transforms.RandomContrast(0.5, 2),
        transforms.RandomSaturation(0.5, 2),
        transforms.RandomFlip(prob=0.5, horizontal=True, vertical=False),
        transforms.RandomFlip(prob=0.5, horizontal=False, vertical=True),
    ]
        class AddAugmentationsTrainer(DefaultTrainer):
            @classmethod
            def build_train_loader(cls, cfg):
                custom_mapper = DatasetMapper(cfg, is_train=True, augmentations=train_augmentations)
                return build_detection_train_loader(cfg, mapper=custom_mapper)

        # カテゴリー名称の設定
        # MetadataCatalog.get(traningDataName).thing_classes = traningMetaData
        # トレーニングデータの設定
        register_coco_instances(traningDataName, {}, CoCoFilePathName, imageRootPath)
        # 学習データの出力
        traningDataMetaData = MetadataCatalog.get(traningDataName)
        #print(traningDataMetaData)
        datasetDicts = DatasetCatalog.get(traningDataName)
        #print(datasetDicts)
        img = cv2.imread(datasetDicts[0]["file_name"])
        visualizer = Visualizer(img[:, :, ::-1], metadata=traningDataMetaData, scale=1.0)
        out = visualizer.draw_dataset_dict(datasetDicts[0])
        cv2.imwrite("./images/tmp.jpg",out.get_image()[:, :, ::-1])
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
        self.trainer = AddAugmentationsTrainer(self.cfg)
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
        im = cv2.imread("./images/input_b.jpg")
        outputs = self.predictor(im)
        # v = Visualizer(im[:, :, ::-1], metadata=traningDataMetaData, scale=1.0)
        v = Visualizer(im[:, :, ::-1], metadata=MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1.0)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        cv2.imwrite("./images/output3.jpg",out.get_image()[:, :, ::-1])