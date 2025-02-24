#!/usr/bin/env python
# coding:utf-8
""" デバック用リロードサーバー起動 """
import uvicorn

def main():
    # デバック用サーバー起動
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)

if __name__ == "__main__":
    main()