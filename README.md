# Chat Service

## Опис

Цей проект реалізує серверну частину веб-сервісу для обміну повідомленнями через WebSocket і REST API. Сервіс дозволяє користувачам реєструватися, логінитися, створювати чати та обмінюватися повідомленнями в реальному часі.

## Структура проекту

```bash
/chat_service/
    ├── auth_service.py       # Сервіс авторизації
    ├── chat_service.py       # Сервіс керування чатами
    ├── message_service.py    # Сервіс WebSocket
    ├── models.py             # Моделі бази даних
    ├── db.py                 # Ініціалізація бази даних
    ├── api_handler.py        # Єдиний API хендлер
    └── main.py               # Головний файл для запуску сервера
```

## Інструкції щодо запуску

### 1. Клонування репозиторію
```bash
git clone https://github.com/ValiguraI/chat_service.git
cd chat_service
```
### 2. Створення віртуального середовища
```bash
python3 -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

### 3. Встановлення залежностей
```bash
pip install -r requirements.txt
```

### 4. Запуск сервера
```bash
python main.py
```

### 5. Тестування API за допомогою curl
Реєстрація користувача
```bash
curl -X POST http://localhost:8000/auth/register -d '{"username": "user1", "password": "pass"}' -H "Content-Type: application/json"
```
Логін користувача
```bash
curl -X POST http://localhost:8000/auth/login -d '{"username": "user1", "password": "pass"}' -H "Content-Type: application/json"
```
Створення чату
```bash
curl -X POST http://localhost:8000/chats/create -d '{"name": "New Chat"}' -H "Authorization: Bearer <JWT_Token>" -H "Content-Type: application/json"
```
Отримання списку чатів
```bash
curl -X GET http://localhost:8000/chats -H "Authorization: Bearer <JWT_Token>"
```

### 6. Тестування WebSocket через wscat
```bash
wscat -c ws://localhost:8001/ws/chat/1
> Hello, World!
```
