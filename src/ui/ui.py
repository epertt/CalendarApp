from ui.login_view import LoginView
from ui.calendar_view import CalendarView
from ui.date_view import DateView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._date = None

    def start(self):
        self._show_view_login()

    def _reset_view(self, reset_menu=False):
        if self._current_view:
            self._current_view.destroy(reset_menu)
        self._current_view = None

    # maybe just a single function for showing different views?
    def _show_view_login(self, menu_buttons=None):
        self._reset_view()
        self._current_view = LoginView(self._root, self._show_view_calendar, menu_buttons)
        self._current_view.pack()

    def _show_view_calendar(self):
        self._reset_view()
        self._current_view = CalendarView(self._root, self._show_view_date, self._show_view_login)
        self._current_view.pack()

    def _show_view_date(self, date):
        self._reset_view()
        self._current_view = DateView(self._root, date, self._show_view_calendar, self._show_view_login)

    def _show_view_configuration(self):
        pass

    def _show_view_note(self):
        pass

    def _show_view_help(self):
        pass
