import sqlite3


DB_NAME = "database.db"

def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS excel_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        url TEXT,
        xpath TEXT,
        price REAL,
        avg_price REAL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')

    connection.commit()
    connection.close()


create_database()

