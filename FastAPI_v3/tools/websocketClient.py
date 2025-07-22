# 簡易WebSocket Client
import asyncio
import websockets


async def send_task(websocket):
    while True:
        msg = await asyncio.get_event_loop().run_in_executor(None, input, "Send message (or 'exit' to quit): ")
        if msg.lower() == "exit":
            print("Exiting WebSocket client.")
            await websocket.close()
            return
        await websocket.send(msg)

async def recv_task(websocket):
    try:
        async for response in websocket:
            print(f"\nReceived: {response}")
    except websockets.ConnectionClosed:
        pass


async def websocket_client():
    """
    WebSocketクライアントのサンプルコード
    """
    uri = "ws://localhost:8000/ws/echo"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server.")
        try:
            # 入力と受信を同時に処理するため、2つのタスクを作成
            send = asyncio.create_task(send_task(websocket))
            recv = asyncio.create_task(recv_task(websocket))
            await asyncio.wait([send, recv], return_when=asyncio.FIRST_COMPLETED)
        except websockets.ConnectionClosed:
            print("WebSocket connection closed.")
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(websocket_client())