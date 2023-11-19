import datetime

class Date:

    __init__(self, year=1970, month=1, day=1, notes=None):

        self.date = datetime.date(year, month, day)
        self.notes = notes