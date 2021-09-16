#!/usr/bin/env python
# coding:utf-8
## 標準モジュールのインポート
# 時刻表示
import datetime
## CSVモジュール
import csv

### CSV ファイル操作 #########################################################
def readCSV(filename: str) -> list:
    """ CSVファイル読み込み
        Args: 
            filename: 読み込むファイル名
        Return:
            CSVファイルのヘッダー行をキーにしたディクショナリーのリスト
    """
    with open(filename) as f:
        return [row for row in csv.DictReader(f)]

def writerCSV(filename: str,datas: list, header: list):
    """ CSVファイル書き込み
        Args: 
            filename: 読み込むファイル名
            datas: csvファイルに出力するディクショナリーのリスト
            header: csvに出力するカラム及びキー
    """
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        # ヘッダー出力
        writer.writerow(header)
        # ヘッダーで指定したデータを出力
        writer.writerows([exportDictToList(dictDataList=data, keyList=header) for data in datas]) 

def exportDictToList(dictDataList: dict, keyList: list) -> list:
    """ 必要データの取り出し
        辞書のリストから、指定したキーの値をリストとして取り出し
        Args: 
            dictDataList: 元のディクショナリーのリスト
            keyList: 取り出す値
        Return:
            指定したキーの値リストとして返す
    """
    return [dictDataList[key] for key in keyList] 

### ログ出力 ##############################################################
def nowdate() -> str:
    """ 現在時刻表示文字列 RFC3339 +9H"""
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+09:00")

