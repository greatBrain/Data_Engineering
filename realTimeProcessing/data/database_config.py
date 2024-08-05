import psycopg2 as pos

""" WARNING
Never, never write our passwords, API keys, configuration keys and any kind of access in plain text
or inside the code base. The recommended manner is environment variables or .env files.
Just for testing and practices purposes i've done it.
"""

def connect_to_db():

    with pos.connect(
         dbname = "weather_real_time",
         user = "postgres",
         password = "EMem232213",
         host = "localhost",
         port = "5432"

    )as conn:
        return conn
