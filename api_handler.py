import json
from http.server import BaseHTTPRequestHandler
from auth_service import register_user, login_user
from chat_service import create_chat, get_chats

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def _send_response(self, response_code, data):
        self.send_response(response_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    # Обробка POST-запитів (реєстрація, логін, створення чату)
    def do_POST(self):
        if self.path == '/auth/register':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data)

            username = post_data.get('username')
            password = post_data.get('password')

            register_user(username, password)
            response = {"message": "User registered successfully"}
            self._send_response(200, response)

        elif self.path == '/auth/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data)

            username = post_data.get('username')
            password = post_data.get('password')

            token = login_user(username, password)
            if token:
                response = {"token": token}
                self._send_response(200, response)
            else:
                self._send_response(401, {"message": "Invalid credentials"})

        elif self.path == '/chats/create':
            token = self.headers.get('Authorization')
            if not token:
                self._send_response(401, {"message": "Unauthorized"})
                return

            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data)

            chat_name = post_data.get('name')
            create_chat(chat_name)
            response = {"message": "Chat created successfully"}
            self._send_response(200, response)

    # Обробка GET-запитів (отримання списку чатів)
    def do_GET(self):
        if self.path == '/chats':
            token = self.headers.get('Authorization')
            if not token:
                self._send_response(401, {"message": "Unauthorized"})
                return

            chats = get_chats()
            response = {"chats": chats}
            self._send_response(200, response)
