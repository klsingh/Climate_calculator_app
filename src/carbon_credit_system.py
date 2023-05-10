import sqlite3

DATABASE_PATH = 'db/climate_calculator.db'

class CreditPointTracker:
    def __init__(self, user_id):
        self.user_id = user_id
        self.credit_points = self.get_credit_points()

    def get_credit_points(self):
        """
        Returns the user's current credit point balance.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT credit_points FROM users WHERE id = ?', (self.user_id,))
            credit_points = cursor.fetchone()[0]
            return credit_points

    def add_credit_points(self, amount):
        """
        Adds the specified amount of credit points to the user's balance.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET credit_points = credit_points + ? WHERE id = ?', (amount, self.user_id))
            conn.commit()
        self.credit_points += amount

    def deduct_credit_points(self, amount):
        """
        Deducts the specified amount of credit points from the user's balance.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET credit_points = credit_points - ? WHERE id = ?', (amount, self.user_id))
            conn.commit()
        self.credit_points -= amount
