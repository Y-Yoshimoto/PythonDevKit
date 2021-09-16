#!/usr/bin/env python
# coding:utf-8
## 標準モジュールのインポート
import json

# Reids接続
import RedisConnector.Connector as RedisC
RC = RedisC.Connector(host='redis_c', db=0, port=6379)

def main():
    print("Hellow World!")
    RC.regist(key="key1",value="item1")
    v=RC.get(key="key1")
    print(v)
    
    RC.regist(key="key2",value="item2")
    v=RC.get(key="key2")
    print(v)

if __name__ == '__main__':
    main()
