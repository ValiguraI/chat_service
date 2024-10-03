from models import get_db_connection
from auth_service import verify_jwt

# Створення чату
def create_chat(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chats (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Отримання списку чатів
def get_chats():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chats")
    chats = cursor.fetchall()
    conn.close()
    return chats
