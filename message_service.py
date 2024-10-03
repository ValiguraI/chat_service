import asyncio
import websockets
from models import get_db_connection

clients = []

async def websocket_handler(websocket, path):
    clients.append(websocket)
    chat_id = path.split('/')[-1]

    try:
        async for message in websocket:
            for client in clients:
                if client != websocket:
                    await client.send(f"Message: {message}")
            # Збереження повідомлення в базу даних
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages (chat_id, user_id, message) VALUES (?, ?, ?)", (chat_id, 1, message))
            conn.commit()
            conn.close()
    finally:
        clients.remove(websocket)

# Функція для запуску WebSocket сервера
async def run_websocket_server():
    print("Starting WebSocket server...")
    async with websockets.serve(websocket_handler, "localhost", 8001):
        await asyncio.Future()  # Блокування для утримання сервера запущеним