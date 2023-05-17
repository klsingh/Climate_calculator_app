import sqlite3
import hashlib

DATABASE_PATH = 'db/climate_calculator.db'

class UserAuthentication:
    def __init__(self):
        pass
    
    def login(self, username, password):
        """
        Authenticates the user's credentials.
        Returns True if authentication is successful, else False.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()
            if result and result[0] == password:
                return True
            else:
                return False

    def register(self, username, password, email):
        """
        Registers a new user with the specified credentials.
        Returns True if registration is successful, else False.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()
            if result:
                return False
            else:
                cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
                conn.commit()
                return True
    def hash_password(password):
        salt = "a_random_string_for_salt" # Generate a random string for the salt
        salted_password = salt + password
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        return hashed_password
