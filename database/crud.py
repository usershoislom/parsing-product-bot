import sqlite3
from database.database import DB_NAME


def save_user_data(user_id: int):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT OR IGNORE INTO users (user_id) VALUES (?)
        ''', (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Не удалось добавить пользователя: {e}")
    finally:
        conn.close()


def save_excel_data(user_id: int, title: str, url: str, xpath: str, price: str):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO excel_data (user_id, title, url, xpath, price) VALUES (?, ?, ?, ?, ?)
        ''', (user_id, title, url, xpath, price))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Не удалось добавить данные: {e}")
    finally:
        conn.close()


def get_user_data(user_id: int):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
        SELECT user_id, title, url, xpath, price
        FROM excel_data
        WHERE user_id = ?;
        ''', (user_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Не удалось получить данные из бд: {e}")
        return []
    finally:
        conn.close()
