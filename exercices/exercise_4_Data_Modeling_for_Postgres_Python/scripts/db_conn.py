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
        run_sql_script(cursor) 

    except (Exception, psycopg2.Error) as error:
            print("Error when connecting to PostgreSQL", error)
            return False

    finally:
        if conn:
           cursor.close()
           conn.close()
           return True

# Execute sql script
def run_sql_script(cursor) -> bool:
    with open('statements.sql', 'r') as sql_file:
         sql_statements = sql_file.read()
         cursor.execute(sql_statements)
         return True
