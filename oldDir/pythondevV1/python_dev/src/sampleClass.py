#!/usr/bin/env python
# coding:utf-8
import sys
import json

class sampleC:
    """ Jsonファイルの読み込み/表示クラス """
    def __init__ (self, filename):
        print("Init")
        #self.jsonData = json.load(open(filename, 'r'))
        try:
            self.jsonData = json.load(open(filename, 'r'))
        except FileNotFoundError:
            print("File Not Found Error")
            sys.exit()

    def __del__(self):
        print("Dell")

    def showAll(self):
        print(self.jsonData)

    def showData(self):
        print(self.jsonData["data"])

    def showType(self):
        print(type(self.jsonData))