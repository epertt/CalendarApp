import sqlite3
from config import DB_FILE_PATH

connection = sqlite3.connect(DB_FILE_PATH)
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection

def initialize_for_testing():
    cursor = connection.cursor()
    cursor.execute("drop table if exists users;")
    cursor.execute("create table users ( username text primary key, password text );")
    cursor.execute("insert into users(username, password) values('user', 'pass');")
    connection.commit()

if __name__ == "__main__":
    initialize_for_testing()
