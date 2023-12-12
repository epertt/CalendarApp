from create_schema import initialize_db


def setup():
    """Initializes the database. Usually called from the command
    line or before running tests.
    """
    initialize_db()


if __name__ == "__main__":
    setup()
