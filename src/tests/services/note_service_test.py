import unittest
import datetime
from entities.note import Note
from entities.user import User

from services.note_service import NoteService


class FakeNoteRepository:
    def __init__(self, notes=None):
        self.notes = notes or []

    def get_notes_by_date(self, user_id, date):
        note = list(
            filter(
                lambda u: u is not None and u.user_id is user_id and u.date is date, self.notes)
        )
        return list(note) if len(note) > 0 else None

    def get_note_by_id(self, note_id):
        note = list(
            filter(lambda u: u is not None and u.note_id == note_id, self.notes))
        return note[0] if len(note) > 0 else None

    def get_notes_all(self, user_id):
        note = list(
            filter(lambda u: u is not None and u.user_id == user_id, self.notes))
        return list(note) if len(note) > 0 else None

    def create_note(self, note):
        note = Note(note.user_id, note.date, note.content, len(self.notes))
        self.notes.append(note)
        return self.get_note_by_id(note.note_id)

    def delete_note(self, note):
        note_index = self.notes.index(note)
        self.notes = self.notes[:note_index]+[None]+self.notes[note_index+1:]
        return self.get_note_by_id(note.note_id)


class TestNoteService(unittest.TestCase):
    def setUp(self):
        self.fake_note_repo = FakeNoteRepository()
        self.note_service = NoteService(self.fake_note_repo)

        self.date1 = datetime.datetime(2022, 1, 1)
        self.date2 = datetime.datetime(2023, 2, 2)

        self.user1 = User("name1", "pass1", 0)
        self.user2 = User("name2", "pass2", 1)

        self.test_notes = []
        self.test_notes.append(
            Note(self.user1.user_id, self.date1.timestamp(), "some text", len(self.test_notes)))
        self.test_notes.append(
            Note(self.user2.user_id, self.date2.timestamp(), "some other text", len(self.test_notes)))

        self.note_service.add_note(self.user1, self.date1, "some text")
        self.note_service.add_note(self.user2, self.date2, "some other text")

    def test_add_note(self):
        date3 = datetime.datetime(2024, 3, 3)
        user3 = User("name3", "pass3", 2)
        created_note = self.note_service.add_note(
            user3, date3, "testtext"
        )

        test_note = Note(user3.user_id, date3.timestamp(),
                         "testtext", len(self.test_notes))
        self.test_notes.append(test_note)

        self.assertEqual(
            created_note,
            self.test_notes[len(self.test_notes)-1]
        )

    def test_delete_note(self):
        self.assertEqual(
            self.note_service.remove_note(self.test_notes[0]),
            None
        )
