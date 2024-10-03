import threading
from http.server import HTTPServer
from chat_service import create_chat, get_chats
from auth_service import register_user, login_user
from message_service import run_websocket_server
from models import init_db
from api_handler import SimpleAPIHandler
import asyncio

# HTTP сервер для REST API
def run_http_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print('Starting HTTP server...')
    httpd.serve_forever()

# Функція для запуску WebSocket сервера
def run_ws_server():
    asyncio.run(run_websocket_server())

# Головна функція для запуску всіх сервісів
if __name__ == "__main__":
    init_db()  # Ініціалізація бази даних

    # Запуск HTTP сервера у потоці
    threading.Thread(target=run_http_server).start()

    # Запуск WebSocket сервера в основному потоці асинхронно
    run_ws_server()