from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

# 転送先のWeb APIサーバーのURL
TARGET_API_BASE_URL = "https://api.open-meteo.com/v1/"
# サンプル
# https://api.open-meteo.com/v1/forecast?latitude=35.6785&longitude=139.6823&current_weather=true

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def reverse_proxy(path: str, request: Request):
    # 転送先のURLを構築
    target_url = f"{TARGET_API_BASE_URL}/{path}"

    # 転送元リクエストのヘッダーやボディを取得
    headers = dict(request.headers)
    body = await request.body()

    # HTTPリクエストを別のサーバに転送
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            content=body
        )

    # 特定のパスに対するレスポンスのボディを書き換え
    if path.startswith("specific-path"):
        if response.headers.get("Content-Type") == "application/json":
            original_body = response.json()
            # ボディの一部を書き換える例
            original_body["modified_key"] = "modified_value"
            return JSONResponse(content=original_body, status_code=response.status_code, headers=response.headers)

    # レスポンスをそのまま返却
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )
