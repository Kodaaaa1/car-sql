import sqlite3

def connect():
    return sqlite3.connect('data/maintenance.db')

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    with open('database/schema.sql', 'r') as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
