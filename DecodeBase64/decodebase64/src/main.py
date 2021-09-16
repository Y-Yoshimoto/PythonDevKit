#!/usr/bin/env python
# coding:utf-8
## XMLモジュールのインポート
import xml.etree.ElementTree as ET

## Base64 モジュール
import base64

## ログ出力用
import datetime
def nowdate() -> str:
    """ 現在時刻表示文字列 RFC3339 +9H"""
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+09:00")

### データ整形 ###################################################
def extractFileInfo(recode: dict) -> dict:
    """XMLの特定階層から、ファイル取り出しに必要なデータを抽出
        args:
            recode: XMLから取り出した1階層
        return
            ファイル情報及びファイルデータ
    """
    # 確認用print文
    #print("---------------------------------------------")
    #print(f'recode: {recode.attrib["name"]}')
    #print(f'id: {recode.find("id").text}')
    #print(f'filename: {recode.find("filename").text}')
    #print(f'data: {recode.find("data").text}')
    print(f'{nowdate()}, Convert {recode.find("id").text}: {recode.find("filename").text}.')
    returnData = {'recode': recode.attrib["name"],
            'id': recode.find("id").text,
            'filename': recode.find("filename").text,
            # 'dataBase64': recode.find("data").text, #確認用
            'dataROW': decodeBase64(base64Str = recode.find("data").text)
            }
    return returnData


### Base64デコード ###################################################
def decodeBase64(base64Str: str) -> str:
    """Base64の文字列を受け取り、バイナリにデコードして返す
        args:
            base64Str: Base64文字列
        return
            デコード済みのバイナリデータ
    """
    returnStr = base64.urlsafe_b64decode(base64Str)
    return returnStr


### ファイル出力 ###################################################
def ExportBinaryFile(filepath: str, data: bytes):
    """バイナリデータをファイルとして書き出す
        args:
            base64Str: Base64文字列
            data: 出力するバイナリデータ
        return
            ステータスコード
    """
    print(f'{nowdate()}, Export {filepath}.')
    with open(filepath, mode='wb') as f:
        f.write(data)


### main文 ###################################################
def main():
    print(f'{nowdate()}, Info, Read XML files.')
    # XMLデータ読み込み、第一階層でリストとして取り出し
    root = ET.parse('./inputFile/sample2.xml').getroot()
    # ファイル出力に必要なタグの情報を取り出し/ファイルデコード   
    files = [extractFileInfo(recode = child) for child in root]
    # デコードファイル出力
    status = [ExportBinaryFile(filepath= "./outputFile/" + file['id'] +'-'+ file['filename'],
                                data = file['dataROW']) for file in files]

if __name__ == '__main__':
    main()

