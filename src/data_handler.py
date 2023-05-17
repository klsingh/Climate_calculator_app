import csv
import json
import os
import sqlite3

DATABASE_PATH = 'db/climate_calculator.db'
CARBON_DATA_PATH = 'data/carbon_data.csv'
CREDIT_POINTS_PATH = 'data/credit_points.json'
USERS_PATH = 'data/users.json'

class DataHandler:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()
        self.create_tables()
        
    def create_tables(self):
        """
        Creates the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT UNIQUE,
                credit_points INTEGER DEFAULT 0
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS carbon_footprint_data (
                id INTEGER PRIMARY KEY,
                activity TEXT UNIQUE,
                carbon_emissions INTEGER
            )
        ''')
        
        self.connection.commit()
        
    def load_users(self):
        """
        Loads user data from the users.json file and inserts it into the users table.
        """
        with open(USERS_PATH) as f:
            users = json.load(f)
            for user in users:
                self.cursor.execute('''
                    INSERT INTO users (username, password, email, credit_points)
                    VALUES (?, ?, ?, ?)
                ''', (user['username'], user['password'], user['email'], user['credit_points']))
            self.connection.commit()
            
    def load_carbon_data(self):
        """
        Loads carbon footprint data from the carbon_data.csv file and inserts it into the carbon_footprint_data table.
        """
        with open(CARBON_DATA_PATH) as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader:
                self.cursor.execute('''
                    INSERT INTO carbon_footprint_data (activity, carbon_emissions)
                    VALUES (?, ?)
                ''', (row[0], row[1]))
            self.connection.commit()
            
    def load_credit_points(self):
        """
        Loads credit point data from the credit_points.json file and updates the corresponding user records.
        """
        with open(CREDIT_POINTS_PATH) as f:
            credit_points = json.load(f)
            for username, points in credit_points.items():
                self.cursor.execute('''
                    UPDATE users SET credit_points = ?
                    WHERE username = ?
                ''', (points, username))
            self.connection.commit()
    
    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()
