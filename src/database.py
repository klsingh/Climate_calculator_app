import sqlite3

DATABASE_PATH = 'db/climate_calculator.db'

def create_tables():
    """
    Creates the necessary tables in the database.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

def register_user(username, password):
    """
    Registers a new user in the database.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

def authenticate_user(username, password):
    """
    Authenticates a user based on their username and password.
    Returns the user ID if successful, or None if authentication fails.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        if user:
            return user[0]
        else:
            return None
