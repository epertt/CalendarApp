from entities.note import Note

from repositories.note_repository import note_repository as default_note_repository


class NoteService:
    def __init__(self, note_repository=default_note_repository):
        self._note_repository = note_repository

    def get_notes_by_date(self, user, date):
        return self._note_repository.get_notes_by_date(user.user_id, date.timestamp())

    def get_notes_all(self, user):
        return self._note_repository.get_notes_all(user.user_id)

    def add_note(self, user, date, content):
        new_note = Note(user.user_id, date.timestamp(), content)
        return self._note_repository.create_note(new_note)

    def remove_note(self, note):
        return self._note_repository.delete_note(note.note_id)


note_service = NoteService()
