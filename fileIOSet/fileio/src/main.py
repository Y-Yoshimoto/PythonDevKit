#!/usr/bin/env python
# coding:utf-8
## 標準モジュールのインポート
import json

## 自作モジュールの読み込み
import fileIO as fIO

def main():
    print("File IO!")
    ## CSVファイル
    csvFileData = fIO.readCSV(filename = "./sampleData/sampeIn.csv")
    print(csvFileData)
    
    fIO.writerCSV(filename = "./sampleData/sampeOut.csv",
                    datas = csvFileData,
                    header=["Id", "Name"])
    
    ## Jsonファイル
    jsonFileData = fIO.readJSON(filename = "./sampleData/sampleIn.json")
    noNestData = [ fIO.oneNestElimination(x,"data") for x in jsonFileData]

    print(noNestData)  
    fIO.writerCSV(filename = "./sampleData/sampeOutjson.csv",
                    datas = noNestData,
                    header=["data.Max", "data.Min", "delta"])
    
    fIO.writerJSON(filename = "./sampleData/sampeOut.json",
                    datas = noNestData,
                    header=["data.Max", "data.Min"])

    fIO.writerJSONROW(filename = "./sampleData/sampeOutROW.json",
                    datas = noNestData)   

if __name__ == '__main__':
    main()
