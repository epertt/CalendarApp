class Note:
    """Class representing a note
    
        Attributes:
            note_id: a unique integer identifying the note
            user_id: an integer representing user whose note is being represented
            date: a unix epoch timestamp integer used to represent the date
            content: a string representing the content of the note 
    """
    def __init__(self, user_id, date, content, note_id=None):

        self.note_id = note_id
        self.user_id = user_id
        self.date = date
        self.content = content
