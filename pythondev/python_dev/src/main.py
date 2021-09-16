#!/usr/bin/env python
# coding:utf-8
## 標準モジュールのインポート
import json

## 自作モジュールの読み込み
import sampleFunction as sf
import sampleClass as sc

def fortest():
    for i in range(1,10, 2):
        print(i)
    for i in range(10):
        if i % 2 == 0:
            print(i)
        else:
            print("even")

def listtest():
    for i in [x**2 for x in range(1,10)]:
        print(i)

def main():
    print("Hellow World!")
    # fortest()
    #listtest()

    print(range(1,10))

    ## インポートしたサンプル関数の実行
    #sf.echoArg("date")
    #sf.date()


    ## インポートしたサンプルクラスの実行
    scInstance = sc.sampleC("./sample.json")
    scInstance.showType()
    scInstance.showAll()
    scInstance.showData()

if __name__ == '__main__':
    main()
