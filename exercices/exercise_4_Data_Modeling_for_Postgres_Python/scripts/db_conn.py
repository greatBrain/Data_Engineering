import psycopg2
from dotenv import load_dotenv
import os

# Load the variables in .env file
load_dotenv()

def open_conn():
    try:
        conn = psycopg2.connect(
            host = os.getenv('DB_HOST')
            database = os.getenv('DB_NAME')
            user = os.getenv('DB_USER')
            pwd = os.getenv('DB_PASSWORD')
            port = os.getenv('DB_PORT')
        )
        cursor = conn.cursor()

        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        print("Postgres version: {}".format(version))


    except (Exception, psycopg2.Error) as error:
            print("Error when connecting to PostgreSQL", error)

    finally:
        if conn:
           cursor.close()
           conn.close()
           return 
