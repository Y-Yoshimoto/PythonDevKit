#!/usr/bin/env python
# coding:utf-8
import redis

# MongoDB コネクタ
class Connector:
    """Redisコネクター"""
    def __init__ (self, host='redis_c', db=0, port=6379):
        print("__init__", flush=True)
        self.redisC = redis.Redis(host=host, port=port, db=db)

    def __del__(self):
        print("__del__", flush=True)
    #    self._client.close()
    
    ## 登録 #####################################################
    def regist(self, key, value):
        """キーを指定して値を登録"""
        self.redisC.set(key, value)
        
    ## 登録有効期限付き #####################################################
    def regist_ex(self, key, value, ex):
        """キーを指定して値を登録"""
        self.redisC.set(key, value, ex=ex)
        
    ## 参照 ################################################# 
    def get(self, key):
        """キーを指定して値を取得 キーが無い場合 Noneを返す"""
        value = self.redisC.get(key)
        return value.decode() if value is not None else  None
    
    