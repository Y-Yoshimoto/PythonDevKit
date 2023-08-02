#!/usr/bin/env python
# coding:utf-8

# Detectronクラス
import myDetectronModel as DecModel
# 補助関数
import subFunctions as sub
# 処理時間計測
import time
def main():
    print("start")
    start = time.time()
    model1=DecModel.myModel()
    
    # 転移学習前
    # model1.ExecInference_OutputImage(imageFilePathName="./images/input.jpg",
    #                                 OutputFilePathNam="./images/output1.jpg")
    # 
    # sub.PrintLogFormat("Start TransferLearning. ------------")
    # 転移学習
    
    categoriesInfo = sub.readJson("./CoCoSample/trainval.json")["categories"]
    print(categoriesInfo)
    
    # 転移学習実行
    # model1.TransferLearning(traningDataName="CoCoSample", 
    #                         classesName=categoriesInfo,
    #                         CoCoFilePathName="./CoCoSample/trainval.json",
    #                         imageRootPath="./CoCoSample/images")
    
    model1.TransferLearningDataAugmentation(traningDataName="CoCoSample", 
                            classesName=categoriesInfo,
                            CoCoFilePathName="./CoCoSample/trainval.json",
                            imageRootPath="./CoCoSample/images")
    
    sub.PrintLogFormat("End TransferLearning. ------------")    

    # 転移学習後    
    model1.ExecInference_OutputImage(imageFilePathName="./images/input.jpg",
                                    OutputFilePathNam="./images/output2.jpg")
    model1.ExecInference_OutputImage(imageFilePathName="./images/input_b.jpg",
                                    OutputFilePathNam="./images/output3.jpg")
    end = time.time()

    print("end")
    
if __name__ == '__main__':
    main()

