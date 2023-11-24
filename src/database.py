# for testing only
import datetime
###

import sqlite3
from config import DB_FILE_PATH

connection = sqlite3.connect(DB_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_db_connection():
    return connection


def initialize_for_testing():
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("DROP TABLE IF EXISTS notes;")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes ( 
        note_id INTEGER PRIMARY KEY, 
        user_id INTEGER, 
        date TEXT NOT NULL, 
        content TEXT NOT NULL, 
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );""")

    username = "a"
    password = "a"

    cursor.execute(
        "INSERT INTO users(username, password) VALUES(?, ?);", (username, password,))

    testdate = datetime.datetime(2023, 11, 30)
    testdate_epoch = testdate.timestamp()

    user_id = 1
    note = "short note"
    note2 = "also a note but very important and that is why this note is much longer"

    cursor.execute("INSERT INTO notes(user_id, date, content) VALUES(?, ?, ?);",
                   (user_id, testdate_epoch, note,))
    cursor.execute("INSERT INTO notes(user_id, date, content) VALUES(?, ?, ?);",
                   (user_id, testdate_epoch, note2))

    connection.commit()


# if __name__ == "__main__":
initialize_for_testing()
