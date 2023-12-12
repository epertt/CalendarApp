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
    """A class responsible for note-related database actions.
    """
    def __init__(self, connection):

        self._connection = connection

    def get_notes_by_date(self, user_id, date):
        """Returns notes based on user id and date

        Args:
            user_id (Integer): an integer representing the user id of the
            user
            date (Integer): a unix epoch timestamp representing a date

        Returns: an array of Note objects
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE user_id=? AND date=?',
            (user_id, date,)
        )

        row = cursor.fetchall()

        return get_notes_by_rows(row)

    def get_note_by_id(self, note_id):
        """Returns the note specified in note_id

        Args:
            note_id (Integer): an integer representing the note to look up

        Returns: a Note matching the specified note_id, or
        None if a matching note couldn't be found
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE note_id=?',
            (note_id,)
        )

        row = cursor.fetchone()

        return row[0] if row else None

    def get_notes_all(self, user_id):
        """Returns all notes with matching user_id

        Args:
            user_id (Integer): an integer representing the user whose notes
            to look up

        Returns: an array of Note objects for the specified user
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM notes WHERE user_id=?',
            (user_id,)
        )

        row = cursor.fetchall()

        return get_notes_by_rows(row)

    def create_note(self, note):
        """Adds a new note into the database

        Args:
            note (Note): a Note object representing the note to be added

        Returns: a Note object representing the note that was added
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO notes(user_id, date, content) VALUES(?, ?, ?)',
            (note.user_id, note.date, note.content)
        )

        self._connection.commit()

        return self.get_note_by_id(cursor.lastrowid)

    def delete_note(self, note):
        """Removes a note from the database

        Args:
            note (Note): a Note object representing the note to be removed

        Returns: the note_id of the note that was removed
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'DELETE FROM notes WHERE note_id = ?',
            (note.note_id,)
        )

        self._connection.commit()

        return note.note_id


note_repository = NoteRepository(get_db_connection())
