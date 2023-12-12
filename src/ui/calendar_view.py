import calendar
import datetime
from tkinter import ttk, constants

from services.date_service import date_service


class CalendarView():
    def __init__(self, state, root, date_view, login_view, calendar_view, help_view, config_view):
        self._state = state

        self._root = root
        self._root.title("Calendar")

        self._date = self._state.get_current_date()
        self._current_year = self._date.year

        self._show_date_view = date_view
        self._show_login_view = login_view
        self._show_calendar_view = calendar_view
        self._show_help_view = help_view
        self._show_config_view = config_view

        self._menu_frame = None
        self._main_frame = None
        self._year_menu_frame = None
        self._calendar_frame = None

        self._init()

    def pack(self):
        self._menu_frame.pack(side=constants.TOP,
                              fill=constants.X, expand=False)
        self._main_frame.pack(fill=constants.BOTH)

    def destroy(self):
        self._menu_frame.destroy()
        self._main_frame.destroy()

    def _log_out(self):
        self._state.logout()
        self._show_login_view(self._menu_frame)

    def _show_date(self, year, month, day):
        selected_date = datetime.datetime(year, month, day)
        self._state.set_current_date(selected_date)
        self._show_date_view()

    def _display_menu(self):
        items = ["configuration", "help", "log out"]
        buttons = {}
        for i, item in enumerate(items):
            buttons[item] = ttk.Button(
                self._menu_frame, text=item, padding=5, cursor="hand2")
            buttons[item].grid(row=0, column=i, padx=5, pady=10)
        buttons["configuration"].bind("<Button-1>", lambda event: self._handle_config_button())
        buttons["help"].bind("<Button-1>", lambda event: self._handle_help_button())
        buttons["log out"].bind("<Button-1>", lambda event: self._log_out())

    def _display_year_menu(self, year):
        year_button_previous = ttk.Button(
            self._year_menu_frame, text="<", command=lambda: self._handle_year_button_previous())
        year_button_current = ttk.Button(self._year_menu_frame, text=year)
        year_button_next = ttk.Button(
            self._year_menu_frame, text=">", command=lambda: self._handle_year_button_next())
        year_button_previous.grid(row=0, column=0, padx=5, pady=5)
        year_button_current.grid(row=0, column=1, padx=5, pady=5)
        year_button_next.grid(row=0, column=2, padx=5, pady=5)

    def _display_months(self, month_range=range(1, 13)):
        row = col = 0

        month_frame_width = 200
        month_frame_height = 200

        for month in month_range:
            month_calendar = calendar.monthcalendar(self._current_year, month)

            month_frame = ttk.Frame(self._calendar_frame, borderwidth=1, relief="solid",
                                    width=month_frame_width, height=month_frame_height,
                                    padding=(3, 15, 0, 0))
            month_frame.grid(row=row, column=col, padx=10, pady=10)
            month_frame.grid_propagate(False)

            # TODO: clicking one of these should open a month view for that month
            month_name = calendar.month_name[month]
            month_button = ttk.Button(month_frame, text=month_name)
            month_button.grid(row=0, column=0, columnspan=7, pady=(0, 15))

            for day_name in calendar.day_name:
                day_label = ttk.Label(month_frame, text=day_name[:3], width=-3)
                day_label.grid(row=1, column=list(
                    calendar.day_name).index(day_name), pady=(0, 5))

            for week in month_calendar:
                for day in week:
                    if day > 0:
                        if datetime.date(self._current_year, month, day) == datetime.date.today():
                            day_label = ttk.Label(month_frame, text=str(
                                day), cursor="hand2", width=-2, background='yellow')
                        else:
                            day_label = ttk.Label(month_frame, text=str(
                                day), cursor="hand2", width=-2)
                        day_label.grid(row=month_calendar.index(
                            week) + 2, column=week.index(day))
                        day_label.bind("<Button-1>", lambda event, y=self._current_year,
                                       m=month, d=day: self._show_date(y, m, d))

            col += 1
            if col == 3:
                col = 0
                row += 1

    def _handle_year_button_previous(self):
        previous_year = date_service.get_year_previous(self._date)
        self._state.set_current_date(previous_year)
        self._show_calendar_view()

    def _handle_year_button_next(self):
        next_year = date_service.get_year_next(self._date)
        self._state.set_current_date(next_year)
        self._show_calendar_view()

    def _handle_help_button(self):
        self._show_help_view()

    def _handle_config_button(self):
        self._show_config_view()

    def _init(self):
        self._menu_frame = ttk.Frame(self._root, padding=10)

        self._main_frame = ttk.Frame(self._root, padding=10)

#        self.pack()

        self._year_menu_frame = ttk.Frame(self._main_frame)
        self._year_menu_frame.pack()

        self._calendar_frame = ttk.Frame(self._main_frame)
        self._calendar_frame.pack()

        self._display_menu()
        self._display_year_menu(self._current_year)
        self._display_months()
