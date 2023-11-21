from ui.login_view import LoginView
from ui.calendar_view import CalendarView
from ui.create_user_view import CreateUserView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_view_login()

    def _reset_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_view_login(self):
        self._reset_view()
        self._current_view = LoginView(self._root, self._show_view_calendar)
        self._current_view.pack()

    def _show_view_calendar(self):
        self._reset_view()

        self._current_view = CalendarView(self._root, self._show_view_login)

        self._current_view.pack()

    def _show_view_configuration(self):
        pass

    def _show_view_note(self):
        pass
