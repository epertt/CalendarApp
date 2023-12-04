from tkinter import ttk, constants
from services.date_service import date_service
from services.note_service import note_service


class DateView():
    def __init__(self, state, root, calendar_view, date_view):
        self._state = state

        self._root = root

        self._user = self._state.get_current_user()
        self._date = self._state.get_current_date()
        self._notes = []

        self._root.title(self._date)

        self._show_calendar_view = calendar_view
        self._show_date_view = date_view

        self._add_note_entry = None
        self._add_note_button = None
        self._remove_button = None
        self._note_label_num = None
        self._note_label_content = None

        self._date_menu_frame = None
        self._date_frame = None

        self._init()

    def pack(self):
        self._main_frame.pack(fill=constants.BOTH, expand=True)
        self._date_frame.pack()

    def destroy(self):
        self._main_frame.destroy()

    def _display_date(self):
        year, month, day = self._date.year, self._date.month, self._date.day
        date_label = ttk.Label(self._date_frame, font=(
            "Arial", 15), text=f"{year}/{month}/{day}",
            borderwidth=1, relief="solid", anchor=constants.CENTER)
        date_label.grid(row=0, column=0, columnspan=3,
                        padx=5, pady=5, sticky=constants.NSEW)

    def _display_notes(self):
        self._notes = note_service.get_notes_by_date(self._user, self._date)
        if self._remove_button or self._note_label_content or self._note_label_num:
            for i, _ in enumerate(self._note_label_num):
                self._note_label_num[i].destroy()
            for i, _ in enumerate(self._note_label_content):
                self._note_label_content[i].destroy()
            for i, _ in enumerate(self._remove_button):
                self._remove_button[i].destroy()
        self._note_label_content = {}
        self._note_label_num = {}
        self._remove_button = {}
        for i, note in enumerate(self._notes):
            self._note_label_num[i] = ttk.Label(
                self._date_frame, text=f"{i}:", anchor=constants.CENTER)
            self._note_label_num[i].grid(row=i+1, column=0, padx=5,
                                         pady=5, sticky=constants.NSEW)
            self._note_label_content[i] = ttk.Label(
                self._date_frame, text=f"{note.content}")
            self._note_label_content[i].grid(row=i+1, column=1, padx=5,
                                             pady=5, sticky=constants.NSEW)
            self._remove_button[i] = ttk.Button(
                self._date_frame, text="x", command=lambda
                i=i: self._handle_delete_note_button(self._notes[i]))
            self._remove_button[i].grid(
                row=i+1, column=2, padx=5, pady=5, sticky=constants.NSEW)
        self._display_note_buttons()

    def _display_note_buttons(self):
        if self._add_note_entry:
            self._add_note_entry.destroy()
        self._add_note_entry = ttk.Entry(self._date_frame)
        self._add_note_entry.grid(row=len(self._notes)+1, column=0,
                                  columnspan=2, padx=5, pady=5, sticky=constants.NSEW)

        if self._add_note_button:
            self._add_note_button.destroy()
        self._add_note_button = ttk.Button(
            self._date_frame, padding=5, text="add note", cursor="hand2", command=lambda:
            self._handle_add_note_button())
        self._add_note_button.grid(row=len(self._notes)+1, column=2,
                                   padx=5, pady=5, sticky=constants.NSEW)

    def _display_date_menu_buttons(self):
        date_button_previous = ttk.Button(
            self._date_menu_frame, text="<", command=lambda: self._handle_date_button_previous())
        date_button_current = ttk.Button(
            self._date_menu_frame, text="back", command=lambda: self._handle_calendar_view_button())
        date_button_next = ttk.Button(
            self._date_menu_frame, text=">", command=lambda: self._handle_date_button_next())
        date_button_previous.grid(row=0, column=0, padx=5, pady=5)
        date_button_current.grid(row=0, column=1, padx=5, pady=5)
        date_button_next.grid(row=0, column=2, padx=5, pady=5)

    def _handle_add_note_button(self):
        note_content = self._add_note_entry.get()
        note_service.add_note(self._user, self._date, note_content)
        self._display_notes()

    def _handle_delete_note_button(self, note):
        note_service.remove_note(note)
        self._display_notes()

    def _handle_date_button_previous(self):
        yesterday = date_service.get_day_previous(self._date)
        self._state.set_current_date(yesterday)
        self._show_date_view()

    def _handle_date_button_next(self):
        tomorrow = date_service.get_day_next(self._date)
        self._state.set_current_date(tomorrow)
        self._show_date_view()

    def _handle_calendar_view_button(self):
        self._show_calendar_view()

    def _init(self):

        self._menu_frame = ttk.Frame(self._root, padding=10)
        self._main_frame = ttk.Frame(self._root, padding=10)

        self._date_menu_frame = ttk.Frame(self._main_frame)
        self._date_menu_frame.pack()
        self._display_date_menu_buttons()

        self._date_frame = ttk.Frame(
            self._main_frame, borderwidth=1, relief="solid")

        self._display_date()
        self._display_notes()

        self.pack()
