#!/usr/bin/env python
# coding:utf-8

import MongoConnector.Connector as MongoC

def main():
    # Salesforce接続クライアント インスタンス生成/認証
    print("--- TestRan ---", flush=True)
    
    MC = MongoC.Connector("Sampledb")

    # データ初期化
    MC.dropCollection('Sample1')
    MC.dropCollection('Sample2')
    MC.dropCollection('Sample3')
    MC.dropCollection('Sample4')

    # コレクション一覧1
    print("--- Listup Collection 1 ---", flush=True)
    print(MC.listupCollection(), flush=True)

    # テストデータ登録
    MC.insertData('Sample1', {'key1': 1, 'Value': 100})
    MC.insertData('Sample1', {'key1': 2, 'Value': 200})
    MC.insertData('Sample1', {'key1': 3, 'Value': 300})

    MC.insertManydata('Sample2', [{'key2': 1, 'date': "2021/08/02 22:15:53"},
                                    {'key2': 2, 'date': "2021/03/21 11:25:34"},
                                    {'key2': 3, 'date': "2021/05/02 04:56:13"},
                                    {'key2': 4, 'date': "2022/05/02 04:56:13"}])
    MC.addIndex('Sample1', 'key1')
    MC.addIndex('Sample2', 'key2')

    MC.insertData('Sample3', {'key1': 3, 'Value': 300})
    MC.reCreateCollection('Sample3', [{'key3': 1, 'info': {'one': 1, 'three': 3}},{'key3': 2, 'info': {'tow': 2, 'four': 4}}])
    print(MC.getKeys('Sample3'), flush=True)

    # コレクション一覧2
    print("--- Listup Collection 2 ---", flush=True)
    print(MC.listupCollection(), flush=True)

    # 最大/最小値表示
    print("--- Max and Minimum ---", flush=True)
    print(MC.searchMaxValue('Sample2','date'), flush=True)
    print(MC.searchMinimumValue('Sample2','date'), flush=True)

    # 更新リプレイス
    print("--- Update and Replace ---", flush=True)
    print(MC.updateValueMany('Sample2',filter={'key2': 3}, update={"date": "2021/02/12 14:36:22"}), flush=True)
    print(MC.replaceData('Sample3',filter={'key3': 1}, data={'key3': 1, 'info': {'one': 1, 'tow': 2}}), flush=True)

    ## アップサート
    print("--- Upsert data ---", flush=True)
    print(MC.upsertData('Sample2',filter={'key2': 3}, update={"date": "2021/02/19 14:36:22"}), flush=True)
    print(MC.upsertData('Sample2',filter={'key2': 1}, update={"date": "2021/02/20 14:36:22"}), flush=True)
    print(MC.upsertData('Sample2',filter={'key2': 5}, update={"date": "2021/02/25 14:36:23"}), flush=True)
    print(MC.upsertData('Sample2',filter={'key2': 6}, update={"date": "2021/05/19 14:36:22"}), flush=True)


    # データ削除
    print("--- Delete data ---", flush=True)
    print(MC.deleteDataMany('Sample2', filter={'key2': 3}), flush=True)
    print(MC.deleteDataAndGet('Sample2', filter={'key2': 4}), flush=True)


    # バルク処理
    print("--- Bulk data ---", flush=True)
    MC.insertManydata('Sample4', [{'key2': 1, 'date': "2021/08/02 22:15:53"},
                                    {'key2': 2, 'date': "2021/03/21 11:25:34"},
                                    {'key2': 3, 'date': "2021/05/02 04:56:13"},
                                    {'key2': 4, 'date': "2022/05/02 04:56:13"}])
    
    # データ表示
    print("--- Show All data ---", flush=True)
    print('Sample1: \n' + str(MC.getAllData('Sample1')), flush=True)
    print('Sample2: \n' + str(MC.getAllData('Sample2')), flush=True)
    print('Sample3: \n' + str(MC.getAllData('Sample3')), flush=True)
    print('Sample4: \n' + str(MC.getAllData('Sample4')), flush=True)
    
if __name__ == '__main__':
    main()


