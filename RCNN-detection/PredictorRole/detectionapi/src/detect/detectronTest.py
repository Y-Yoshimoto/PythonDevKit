#!/usr/bin/env python
# coding:utf-8

import myDetectronModel as DecModel


def main():
    #print(torch.__version__, torch.cuda.is_available())
    print("start")
    
    #model=DecModel.zooModel(type="instanceSegmentation")
    model=DecModel.zooModel(type="instanceSegmentation",threshold=0.9)
    #model.ExecInference_OutputImage(imageFilePathName="./sample.jpg",
    #                                OutputFilePathNam="./output.jpg")
    
    b = model.loadLocalImage(fileName="./output.jpg")
    
    #cv2i = model.decodeCV2Image(bImage=b)
    #print(type(cv2i))
    #print(cv2i.shape)
    #bi = model.encodeBytesImage(cv2Image=cv2i)
    
    #model.saveLocalImage(fileName="./sampleOut.jpg", bImage=bi)
    
    li = model.inferenceImage(bImage=b)
    ld = model.inferenceData(bImage=b)
    model.saveLocalImage(fileName="./sampleOut.jpg", bImage=li)
    
    
    # 転移学習前
    # model1.ExecInference_OutputImage(imageFilePathName="./images/input.jpg",
    #                                 OutputFilePathNam="./images/output1.jpg")
    # 
    # sub.PrintLogFormat("Start TransferLearning. ------------")
    # 転移学習
    
    #categoriesInfo = sub.readJson("./CoCoSample/trainval.json")["categories"]
    #print(categoriesInfo)
    
    # 転移学習実行
    # model1.TransferLearning(traningDataName="CoCoSample", 
    #                         classesName=categoriesInfo,
    #                         CoCoFilePathName="./CoCoSample/trainval.json",
    #                         imageRootPath="./CoCoSample/images")
    """
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
    """
    print("end")
    
if __name__ == '__main__':
    main()

