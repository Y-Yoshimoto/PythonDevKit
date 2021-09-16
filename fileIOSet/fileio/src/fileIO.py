#!/usr/bin/env python
# coding:utf-8
## File入出力用関数郡
import csv
import json

# 関数定義
### [dict] データの整形 ######################################################
def exportDictToList(dictDataList: list, keyList: list) -> list:
    """ 必要データの取り出し
        辞書のリストから、指定したキーの値をリストとして取り出し
        Args: 
            dictDataList: 元のディクショナリーのリスト
            keyList: 取り出す値
        Return:
            指定したキーの値リストとして返す
    """
    return [dictDataList[key] for key in keyList] 

def exportDict(dictDataList: list, keyList: list) -> list:
    """ 必要データの取り出し
        辞書のリストから、指定したキーの値のみ出力
        Args: 
            dictDataList: 元のディクショナリーのリスト
            keyList: 取り出す値
        Return:
            指定したキーの値をディクショナリーとして返す
    """
    return  dict(zip([key for key in keyList],[dictDataList[key] for key in keyList]))

def oneNestElimination(dictData: dict, key: str) -> dict:
    """ ディクショナリーのネスト解消　
        辞書の値をkey.orgkey: value として取り出しリスト化する
        Args: 
            dictData: 元のディクショナリーのリスト
            key: 上位階層のキー
        Return:
            辞書値のリストとして返す
    """
    dictData.update(_addkey(dictData[key],key))
    dictData.pop(key)
    return dictData

def _addkey(dictData: dict, key: str) -> dict:
    """ 上位キーの追加 """
    addKey = key + "."
    data = dict(zip([addKey + k for k in dictData],[dictData[k] for k in dictData]))
    return data

### CSV ファイル操作 #########################################################
def readCSV(filename: str) -> list:
    """ CSVファイル読み込み
        Args: 
            filename: 読み込むファイル名
        Return:
            CSVファイルのヘッダー行をキーにしたディクショナリーリスト
    """
    with open(filename) as f:
        return [row for row in csv.DictReader(f)]

def writerCSV(filename: str,datas: list, header: list):
    """ CSVファイル書き込み
        Args: 
            filename: 読み込むファイル名
            datas: csvファイルに出力するディクショナリーリスト
            header: csvに出力するカラム及びキー
    """
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        # ヘッダー出力
        writer.writerow(header)
        # ヘッダーで指定したデータを出力
        writer.writerows([exportDictToList(dictDataList=data, keyList=header) for data in datas]) 


### Json ファイル操作 #########################################################
def readJSON(filename: str) -> list:
    """ CSVファイル読み込み
        Args: 
            filename: 読み込むファイル名
        Return:
            JSON構造のディクショナリーリスト
    """
    return json.load(open(filename, 'r'))

def writerJSON(filename: str,datas: list, header: list):
    """ JSONファイル書き込み
        Args: 
            filename: 読み込むファイル名
            datas: JSON構造のディクショナリーリスト
            header: jsonに出力するカラム及びキー_第一階層
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump([exportDict(dictDataList=data, keyList=header) for data in datas], 
            f, ensure_ascii=False, indent=4)
def writerJSONROW(filename: str,datas: list,):
    """ JSONファイル書き込み - ROW
    Args: 
        filename: 読み込むファイル名
        datas: JSON構造のディクショナリーリスト
        header: jsonに出力するカラム及びキー_第一回想
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(datas, f, ensure_ascii=False, indent=4)
