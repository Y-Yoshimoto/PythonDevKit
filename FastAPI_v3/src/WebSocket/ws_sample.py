# WebSocketのサンプルコード
# 参考: https://fastapi.tiangolo.com/ja/advanced/websockets/#_1
from fastapi import WebSocket, WebSocketDisconnect
from fastapi import APIRouter
import asyncio


router = APIRouter()

# WebSocketのタスクを定義
async def heartbeat_task(websocket: WebSocket):
    """ WebSocketのハートビートを送信する """
    while True:
        try:
            await websocket.send_text("heartbeat")
            await asyncio.sleep(10)  # 10秒ごとにハートビートを送信
        except Exception as e:
            print(f"Heartbeat error: {e}", flush=True)
            break

async def echo_task(websocket: WebSocket):
    """ WebSocketのエコー処理を行う """
    while True:
        try:
            data = await websocket.receive_text()
            print(f"text was: {data}", flush=True)
            await websocket.send_text(f"echo: {data}")
        except WebSocketDisconnect:
            print("WebSocket disconnected", flush=True)

@router.websocket("/ws/echo")
async def websocket_endpoint(websocket: WebSocket):
    """ WebSocket サンプルエコーサーバーのエンドポイント """
    await websocket.accept()
    try:
        heartbeat = asyncio.create_task(heartbeat_task(websocket))
        echo = asyncio.create_task(echo_task(websocket))
        await asyncio.wait([heartbeat, echo], return_when=asyncio.FIRST_COMPLETED)
    except Exception as e:
        await websocket.send_text(f"Error occurred: {str(e)}")
        await websocket.close()
        print(f"Error: {e}", flush=True)
    finally:
        print("WebSocket connection closed", flush=True)
