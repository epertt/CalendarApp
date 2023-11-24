from tkinter import ttk, constants
from services.calendar_service import calendar_service


class DateView():
    def __init__(self, root, date, login_view, calendar_view):
        self._root = root
        self._root.title(date)
        self._root.geometry = ("300x400")

        self._date = date
        self._notes = []

        self._show_calendar_view = calendar_view
        self._show_login_view = login_view


        self._menu_frame = None
        self._date_frame = None

        self._init()

    def pack(self):
        self._main_frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self, logout=False):
        self._main_frame.destroy()

    def _log_out(self):
        calendar_service.logout()
        self._show_login_view()

    def _display_date(self):
        year, month, day = self._date.year, self._date.month, self._date.day
        date_label = ttk.Label(self._date_frame, text=f"{year}/{month}/{day}")
        date_label.grid(row=0, column=0)

    def _display_notes(self):
        self._notes = calendar_service.get_notes(self._date)
        for i, note in enumerate(self._notes):
            note_label = ttk.Label(
                self._date_frame, text=f"{i}: {note.content}")
            note_label.grid(row=i+1, column=0)

    def _display_note_buttons(self):
        items = ["add note", "delete note"]
        buttons = {}

        for i, item in enumerate(items):
            buttons[item] = ttk.Button(
                self._date_frame, padding=5, text=item, cursor="hand2")
            buttons[item].grid(row=i+len(self._notes)+1, column=0)

    def _init(self):

        self._menu_frame = ttk.Frame(self._root)
        self._main_frame = ttk.Frame(self._root)

        self._date_frame = ttk.Frame(
            self._main_frame, borderwidth=1, relief="solid")

        self._display_date()
        self._display_notes()
        self._display_note_buttons()

        self._date_frame.place(in_=self._main_frame,
                               anchor="c", relx=.5, rely=.5)

        self.pack()
