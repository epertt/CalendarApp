from entities.note import Note
from database import get_db_connection


def get_notes_by_rows(row):
    notes = []
    for note in row:
        new_note = Note(note["note_id"], note["user_id"],
                        note["date"], note["content"])
        notes.append(new_note)
    return notes


class NoteRepository:
    def __init__(self, connection):

        self._connection = connection

    def get_notes_by_date(self, user_id, date):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE user_id=? AND date=?',
            (user_id, date)
        )

        row = cursor.fetchall()

        return get_notes_by_rows(row)

    def get_notes_all(self, user_id):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE user_id=?',
            (str(user_id))
        )

        row = cursor.fetchall()

        return get_notes_by_rows(row)

    def create_note(self, user_id, date, note):

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO notes(user_id, date, content) VALUES(?, ?, ?)',
            (user_id, date, note)
        )

        return Note(cursor.lastrowid, user_id, date, note)

    def delete_note(self, note_id):

        cursor = self._connection.cursor()

        cursor.execute(
            'DELETE FROM notes WHERE note_id = ?',
            (str(note_id))
        )

        return note_id


note_repository = NoteRepository(get_db_connection())
