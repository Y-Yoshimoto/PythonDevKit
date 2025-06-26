#!/usr/bin/env python
# coding:utf-8
import uvicorn
from fastapi import FastAPI

# サブモジュール読み込み
from RestSample.apiapp import router as RestSample
from GraphQLSample.apiapp import router as GraphQLSample
from WebSocket.ws_sample import router as ws_sample


# アプリケーション起動
app = FastAPI()
# サブモジュール読み込み
app.include_router(RestSample)
app.include_router(GraphQLSample)
app.include_router(ws_sample)


@app.get("/", include_in_schema=False)
def read_root():
    return {"Path": "root"}


def main():
    # サーバー起動
    uvicorn.run(app=app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
