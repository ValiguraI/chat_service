import jwt
import time
from models import get_db_connection

SECRET_KEY = 'mysecretkey'

# Генерація JWT токена
def generate_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': time.time() + 3600  # Термін дії токена — 1 година
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Перевірка валідності JWT токена
def verify_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded['user_id']
    except jwt.ExpiredSignatureError:
        return None  # Токен протермінований
    except jwt.InvalidTokenError:
        return None  # Невірний токен

# Реєстрація користувача
def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Логін користувача
def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return generate_jwt(user[0])
    return None
