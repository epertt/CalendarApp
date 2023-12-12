import datetime
from dateutil.relativedelta import relativedelta


class DateService:
    def __init__(self):
        self._current_date = datetime.datetime.now()

    def get_day_previous(self, date):
        """Returns the previous day for the given input date

        Args:
            date (Date): a Date object

        Returns:
            Date: a Date 24 hours before the input date
        """
        return date + relativedelta(days=-1)

    def get_day_next(self, date):
        """Returns the following day for the given input date

        Args:
            date (Date): a Date object

        Returns:
            Date: a Date 24 hours after the input date
        """
        return date + relativedelta(days=1)

    def get_year_previous(self, date):
        """Returns the previous year for the given input date

        Args:
            date (Date): a Date object

        Returns:
            Date: a Date 365 days before the input date
        """
        return date + relativedelta(years=-1)

    def get_year_next(self, date):
        """Returns the following year for the given input date

        Args:
            date (Date): a Date object

        Returns:
            Date: a Date 365 days after the input date
        """
        return date + relativedelta(years=1)

    def get_current_date(self):
        """Returns the current date when the program is opened

        Returns:
            Date: a Date representing the current time
        """
        return self._current_date


date_service = DateService()
