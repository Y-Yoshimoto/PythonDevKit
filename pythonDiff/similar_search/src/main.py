#!/usr/bin/env python
# coding:utf-8
"""
    Similar Search　類似度検索
"""
## 標準モジュールのインポート
## 差分比較ライブラリー
import difflib
## 文字全角半角変換
import unicodedata
## 並列処理モジュール
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
## ファイル操作/ログ出力補助関数群
import subFunctions as sub


### 文字列比較関数 #########################################################
def Similar(str1 :str, str2: str, ignoreStr=[""]) -> float:
    """文字列同士を比較し類似度を返す
        全角/半角の正規化、比較時に無視する値を指定
        Args:
            str1: 比較文字列1
            sta2: 比較文字列2
            ignoreStr: 比較時に無視する文字リスト
        Return:
            類似度(1.0=100%)
    """
    n_str1 = unicodedata.normalize('NFKC', str1) # 文字列正規化
    n_str2 = unicodedata.normalize('NFKC', str2) # 文字列正規化
    isjunk = lambda c: c in ignoreStr            # 無視する文字列の設定
    similar = difflib.SequenceMatcher(isjunk=isjunk, a=n_str1, b=n_str2).ratio()
    #print(f'{sub.nowdate()}, Debug, similar is {similar}: {n_str1} and {n_str2}')
    return similar

### マスターデータとの比較 #########################################################
def masterMatch(matchString: str, master: list, mastersKey: str, top=3) -> list:
    """ データをマスタとの比較 キーワード同士の類似度を比較
        マスターデータに類似度を追加し、指定した数のマスターデータを返す
        Args:
            matchString: 比較対象の文字列
            master: 類似度を調べるマスターデータのディクショナリーリスト
            mastersKey: 比較するマスターデータのキー/カラム名を指定
            top: 類似度検索結果の上位数
        Return:
            類似度が高い順に抽出したディクショナリーリスト
        """
    # 類似度計算時に無視する文字を指定
    ignoreStr=[" ", "　", "（",  "）", "(",  ")", "株", "式", "会", "社"]
    
    resultList = [] # Retrn用
    for rowMaster in master:
        ### 類似度を計算し値を類似度をマスターデータに追加
        rowMaster.update({'Similar': Similar(matchString, rowMaster[mastersKey],ignoreStr)})
        resultList.append(rowMaster)  # マスタデータを結果リストに追加
        
    ###  リスト内の辞書のうち、'Similar'の値で並び替えて、topで指定した類似度検索結果の上位数だけを返す
    return sorted(resultList, key=lambda x:x['Similar'],reverse=True)[0:top]
    ##return [ x.update({'Similar': Similar(matchString, x["Name"])}) for x in master][0:top]

def MatchjoinMaster(rowSearchData: dict, master: list, top=3) -> list:
    """ 検索対象行データと検索結果のカラムを指定し結合
        Args:
            rowsearchData: 検索対象行
            master: 検索するマスターのリスト
            top: 検索結果の上位数ディクショナリーリスト
        Return:
            検索対象行と検索結果をまとめたディクショナリーリスト
    """
    # マスターから類似度を用いて検索
    #print(f'{sub.nowdate()}, Info, No.{rowSearchData["No."]}: {rowSearchData["CompanyName"]}')
    SimilarList =  masterMatch(matchString=rowSearchData["CompanyName"], master=master, mastersKey="Name",top=top)
    # 検索結果を検索対象のデータと結合
    for i in range(0,top):
        Similaradd ={"Name_" + str(i+1): SimilarList[i]['Name'],
                    "Similar_" + str(i+1): SimilarList[i]['Similar'],
                    "Code_"+ str(i+1): SimilarList[i]['Code']}
        rowSearchData.update(Similaradd)
    return rowSearchData

def taskParallel(args_):
    """ 並列実行用関数 マスターはグローバルで取得
        Args:
            rowsearchData: 検索対象行
        Retrun:
            検索対象行と検索結果をまとめたディクショナリーリスト
    """
    return MatchjoinMaster(args_,GLOBALMASTER)

### main ###################################################################
def main():
    print(f'{sub.nowdate()}, Info, Start Read CSV files.')
    # マスターデータ読み込み
    master = sub.readCSV(filename="./Master.csv")

    # 検索データ読み込み
    searchData = sub.readCSV(filename="./searchData.csv")
    print(f'{sub.nowdate()}, Info, Successfully read CSV files.')
    print(f'{sub.nowdate()}, Info, Start calculate similarity.')

    # 指定した値でマスター内から類似度の値高い値を取得
    resultLists = []
    
    ''' ### 逐次処理
    for rowSearchData in searchData:
        # マスターデータから類似の高いデータトップ3を取得
        rowResult = MatchjoinMaster(rowSearchData,master)
        resultLists.append(rowResult)
        # print(f'{sub.nowdate()}, Info, No.{rowSearchData["No."]}: {rowSearchData["CompanyName"]}')
    '''
    
    ### 並列処理
    global GLOBALMASTER   # マスターデータをグローバル定数として定義
    GLOBALMASTER = master # マスターデータをグローバル定数に格納
    with ProcessPoolExecutor(8) as executor:
        result = executor.map(taskParallel, searchData)
    resultLists = [r for r in result]

    # マッチングデータ書き込み
    ## エクスポートするカラムを指定
    #print(f'{sub.nowdate()}, Debug, {resultLists[0].keys()}')
    header=["No.", "Email", "CompanyName", 
            "Name_1", "Similar_1", "Code_1", 
            "Name_2", "Similar_2", "Code_2", 
            "Name_3","Similar_3", "Code_3", ]
    sub.writerCSV(filename='Similar.csv',datas=resultLists, header=header)
    print(f'{sub.nowdate()}, Info, Successfully Write CSV files.')

if __name__ == '__main__':
    main()

