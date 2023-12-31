from database import get_db_connection
connection = get_db_connection()


def drop_tables(cursor):
    """Removes database tables

    Args:
        cursor (Cursor): executes SQLite statements
    """
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("DROP TABLE IF EXISTS notes;")
    cursor.execute("DROP TABLE IF EXISTS config;")
    connection.commit()


def create_tables(cursor):
    """Creates database tables

    Args:
        cursor (Cursor): executes SQLite statements
    """
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
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS config ( 
        user_id INTEGER PRIMARY KEY, 
        single_user INTEGER NOT NULL, 
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );""")
    connection.commit()


def initialize_db():
    """Initializes database by dropping existing tables and creating empty tables.
    """
    db_cursor = connection.cursor()
    drop_tables(db_cursor)
    create_tables(db_cursor)


if __name__ == "__main__":
    initialize_db()
