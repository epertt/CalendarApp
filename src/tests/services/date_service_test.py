import unittest
import datetime

from services.date_service import (
    DateService
)

class TestDateService(unittest.TestCase):
    def setUp(self):
        self.date_service = DateService()

    def test_get_current_date_returns_current_date(self):
        date_now = datetime.datetime.now()
        date_now_date_service = self.date_service.get_current_date()
        self.assertEqual(date_now.strftime('%d%m%y'), date_now_date_service.strftime('%d%m%y'))
    
    def test_get_day_previous_returns_previous_day(self):
        test_date = datetime.date(2024, 3, 10)
        previous_day = datetime.date(2024, 3, 9)
        self.assertEqual(self.date_service.get_day_previous(test_date), previous_day)
    
    def test_get_day_previous_returns_correct_day_on_leap_years(self):
        test_date = datetime.date(2024, 3, 1)
        previous_day = datetime.date(2024, 2, 29)
        self.assertEqual(self.date_service.get_day_previous(test_date), previous_day)

    def test_get_day_previous_returns_correct_day_on_normal_years(self):
        test_date = datetime.date(2023, 3, 1)
        previous_day = datetime.date(2023, 2, 28)
        self.assertEqual(self.date_service.get_day_previous(test_date), previous_day)

    def test_get_day_next_returns_next_day(self):
        test_date = datetime.date(2023, 3, 10)
        next_day = datetime.date(2023, 3, 11)
        self.assertEqual(self.date_service.get_day_next(test_date), next_day)

    def test_get_year_previous_returns_previous_year(self):
        test_date = datetime.date(2023, 3, 10)
        previous_year = datetime.date(2022, 3, 10)
        self.assertEqual(self.date_service.get_year_previous(test_date), previous_year)

    def test_get_year_previous_returns_correct_date_on_leap_years(self):
        test_date = datetime.date(2025, 2, 28)
        previous_year = datetime.date(2024, 2, 28)
        self.assertEqual(self.date_service.get_year_previous(test_date), previous_year)

    def test_get_year_previous_returns_correct_date_on_normal_years(self):
        test_date = datetime.date(2023, 3, 28)
        previous_year = datetime.date(2022, 3, 28)
        self.assertEqual(self.date_service.get_year_previous(test_date), previous_year)

    def test_get_year_next_returns_correct_date_on_leap_years(self):
        test_date = datetime.date(2023, 2, 28)
        next_year = datetime.date(2024, 2, 28)
        self.assertEqual(self.date_service.get_year_next(test_date), next_year)

    def test_get_year_next_returns_correct_date_on_normal_years(self):
        test_date = datetime.date(2022, 3, 28)
        next_year = datetime.date(2023, 3, 28)
        self.assertEqual(self.date_service.get_year_next(test_date), next_year)

    def test_get_year_next_returns_next_year(self):
        test_date = datetime.date(2023, 3, 10)
        next_year = datetime.date(2024, 3, 10)
        self.assertEqual(self.date_service.get_year_next(test_date), next_year)