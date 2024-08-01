# Connecting to database or creating.
import sqlite3 as sq
import os

def get_db_path():
    current_dir = os.path.dirname(__file__)
    db_path = os.path.join(current_dir, "weatherData.db")
    return db_path



def load_data(city_name:str, temp:float, weather_description:str, timestamp:str):
    
    database = get_db_path()

    with sq.connect(database) as conn:
        cursor = conn.cursor()

        # Create the table if not
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature REAL,
                description TEXT,
                timestamp TEXT
            )
        ''')

        # Insert data
        cursor.execute('''
            INSERT INTO weather (city, temperature, description, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (city_name, temp, weather_description, timestamp))

        print("Data loaded successfully!")
