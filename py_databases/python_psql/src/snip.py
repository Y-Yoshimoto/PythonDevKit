#!/usr/bin/env python
# coding:utf-8

from connSample import connect_db, connect_db_pool, connect_db_async_pool
from connSample import DbEndpoint
import asyncio

# DB接続情報の設定
config = DbEndpoint(
    dbname="sampledb",
    user="postgres",
    password="postgres",
    host="postgres_c",
    port=5432
)

def main():
    print("main.py")

    print('1 ---------------------')
    connect_db(config)

    print('2 ---------------------')
    connect_db_pool(config)

    print('3 ---------------------')
    asyncio.run(connect_db_async_pool(config))

    print("Finished database operations")

if __name__ == "__main__":
    main()
