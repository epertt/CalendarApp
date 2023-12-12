from ui.login_view import LoginView
from ui.calendar_view import CalendarView
from ui.date_view import DateView
from ui.help_view import HelpView
from ui.config_view import ConfigView

from services.state_service import state_service


class UI:
    """A class responsible for showing the different screens and passing around the state
    """
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._state = state_service

    def start(self):
        """Starts up the user interface
        """
        self._show_view_login()

    def _reset_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_view_login(self, menu_buttons=None):
        self._reset_view()
        self._current_view = LoginView(
            self._state, self._root, self._show_view_calendar, menu_buttons)
        self._current_view.pack()

    def _show_view_calendar(self):
        self._reset_view()
        self._current_view = CalendarView(
            self._state, self._root, self._show_view_date, self._show_view_login, self._show_view_calendar, self._show_view_help, self._show_view_config)
        self._current_view.pack()

    def _show_view_date(self):
        self._reset_view()
        self._current_view = DateView(
            self._state, self._root, self._show_view_calendar, self._show_view_date)
        self._current_view.pack()

    def _show_view_config(self):
        self._reset_view()
        self._current_view = ConfigView(
            self._state, self._root, self._show_view_calendar)
        self._current_view.pack()

    def _show_view_help(self):
        self._reset_view()
        self._current_view = HelpView(
            self._state, self._root, self._show_view_calendar
        )
        self._current_view.pack()
