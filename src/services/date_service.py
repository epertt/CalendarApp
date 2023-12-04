import datetime
from dateutil.relativedelta import relativedelta


class DateService:
    def __init__(self):
        self._current_date = datetime.datetime.now()

    def get_day_previous(self, date):
        return date + relativedelta(days=-1)

    def get_day_next(self, date):
        return date + relativedelta(days=1)

    def get_year_previous(self, date):
        return date + relativedelta(years=-1)

    def get_year_next(self, date):
        return date + relativedelta(years=1)

    def get_current_date(self):
        return self._current_date


date_service = DateService()
