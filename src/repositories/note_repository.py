from entities.note import Note
from database import get_db_connection


def get_notes_by_rows(row):
    notes = []
    for note in row:
        new_note = Note(note["note_id"], note["user_id"],
                        note["date"], note["content"]) if note else None
        notes.append(new_note)
    return notes


class NoteRepository:
    def __init__(self, connection):

        self._connection = connection

    def get_notes(self, user_id, date):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE user_id=? AND date=?',
            (user_id, date,)
        )

        row = cursor.fetchall()

        return get_notes_by_rows(row)

    def create_user(self, user):

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into users(username, password) values(?, ?)',
            (user.username, user.password)
        )

        return user


note_repository = NoteRepository(get_db_connection())
