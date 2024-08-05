import database_config as db

def get_db():
    conn = db.connect_to_db()
    return conn

def create_table():
    conn = get_db()

    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id SERIAL PRIMARY KEY AUTOINCREMENT,
                date DATE NOT NULL,
                temperature FLOAT NOT NULL,
                humidity FLOAT NOT NULL
            )
        ''')
        # Although inside this with manager the commitment is by desault, we make sure of it.
        conn.commit()
