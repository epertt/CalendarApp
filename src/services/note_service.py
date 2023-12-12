from entities.note import Note

from repositories.note_repository import note_repository as default_note_repository


class NoteService:
    """A service responsible for note-related actions
    """
    def __init__(self, note_repository=default_note_repository):
        self._note_repository = note_repository

    def get_notes_by_date(self, user, date):
        """Looks up notes based on the input user and date

        Args:
            user (User): a User object representing the user who's notes to look up
            date (Date): a Date object representing the date for which to look up notes for

        Returns:
            Note[]: an array of Note objects for the specified user and date
        """
        return self._note_repository.get_notes_by_date(user.user_id, date.timestamp())

    def get_notes_all(self, user):
        """Looks up all notes for the input user

        Args:
            user (User): a User object representing the user who's notes to look up

        Returns:
            Note[]: an array of Note objects for the specified user
        """
        return self._note_repository.get_notes_all(user.user_id)

    def add_note(self, user, date, content):
        """Adds a note for the specified user and date

        Args:
            user (User): a User object representing the user to add the note for
            date (Date): a Date object representing the date for which to add the note for
            content (String): a String representing the content of the note

        Returns:
            Note: a Note object representing the added note
        """
        new_note = Note(user.user_id, date.timestamp(), content)
        return self._note_repository.create_note(new_note)

    def remove_note(self, note):
        """Removes a note

        Args:
            note (Note): a Note object representing the note to delete

        Returns:
            Integer: the note id of the removed note
        """
        return self._note_repository.delete_note(note)


note_service = NoteService()
