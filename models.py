import sqlite3

# Ініціалізація бази даних
def init_db():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY, 
                      username TEXT, 
                      password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS chats (
                      id INTEGER PRIMARY KEY, 
                      name TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                      id INTEGER PRIMARY KEY, 
                      chat_id INTEGER, 
                      user_id INTEGER, 
                      message TEXT, 
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Функція для підключення до бази даних
def get_db_connection():
    conn = sqlite3.connect('chat.db')
    return conn
