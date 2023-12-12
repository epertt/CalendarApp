from entities.note import Note
from database import get_db_connection


def get_notes_by_rows(row):
    notes = []
    for note in row:
        new_note = Note(note["user_id"],
                        note["date"],
                        note["content"],
                        note["note_id"]
                        )
        notes.append(new_note)
    return notes


class NoteRepository:
    def __init__(self, connection):

        self._connection = connection

    def get_notes_by_date(self, user_id, date):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE user_id=? AND date=?',
            (user_id, date,)
        )

        row = cursor.fetchall()

        return get_notes_by_rows(row)

    def get_note_by_id(self, note_id):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE note_id=?',
            (note_id,)
        )

        row = cursor.fetchone()

        return row[0]

    def get_notes_all(self, user_id):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE user_id=?',
            (user_id,)
        )

        row = cursor.fetchall()

        return get_notes_by_rows(row)

    def create_note(self, note):

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO notes(user_id, date, content) VALUES(?, ?, ?)',
            (note.user_id, note.date, note.content)
        )

        self._connection.commit()

        return self.get_note_by_id(cursor.lastrowid)

    def delete_note(self, note):

        cursor = self._connection.cursor()

        cursor.execute(
            'DELETE FROM notes WHERE note_id = ?',
            (note.note_id,)
        )

        self._connection.commit()

        return note.note_id


note_repository = NoteRepository(get_db_connection())
