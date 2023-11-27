class Note:

    def __init__(self, user_id, date, content, note_id=None):

        self.note_id = note_id
        self.user_id = user_id
        self.date = date
        self.content = content
