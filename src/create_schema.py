from database import get_db_connection
connection = get_db_connection()


def drop_tables(cursor):
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("DROP TABLE IF EXISTS notes;")
    connection.commit()


def create_tables(cursor):
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
    connection.commit()


def initialize_db():
    db_cursor = connection.cursor()
    drop_tables(db_cursor)
    create_tables(db_cursor)


if __name__ == "__main__":
    initialize_db()
