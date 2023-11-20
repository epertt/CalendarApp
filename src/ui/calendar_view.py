import calendar
import datetime
from tkinter import Tk, ttk, constants

class CalendarView():
    def __init__(self, root):
        self._root = root
        self._root.title("Calendar")
        self._current_year = datetime.datetime.now().year

        self._menu_frame = None
        self._main_frame = None
        self._year_menu_frame = None
        self._calendar_frame = None

        self._init()

    def pack(self):
        self._menu_frame.pack()

    def destroy(self):
        self._root_frame.destroy()

    # wip, should be buttons instead, not functional
    def _display_menu(self):
        items = ["configuration", "add & remove notes", "help", "log out"]
        for i, item in enumerate(items):
            foo = ttk.Label(master=self._menu_frame, text=item, padding=5, borderwidth=1, relief="solid", cursor="hand2")
            foo.grid(row=0, column=i, padx=5, pady=10)

    # wip, should be buttons instead, not functional
    def _display_year_menu(self, year):
        items = ["<", year, ">"]
        for i, item in enumerate(items):
            self.year_label = ttk.Label(self._year_menu_frame, text=items[i], font=("Arial", 25), cursor="hand2")
            self.year_label.grid(row=0, column=i, padx=10)

    # TODO: refactor this (and rest of code) to show configurable amount of months...
    # or just use a different view for year/month view, since week view probably
    # requires that anyway
    def _display_months(self, month_range=range(1, 13)):
        row = col = 0

        # fixed size for each month frame; though not ideal, still looks better 
        # than having mismatched heights for months
        month_frame_width = 220
        month_frame_height = 200
        
        for month in month_range:
            month_calendar = calendar.monthcalendar(self._current_year, month)

            # a separate frame for each month is needed to use grid
            month_frame = ttk.Frame(self._calendar_frame, borderwidth=1, relief="solid", width=month_frame_width, height=month_frame_height, padding=(6, 15, 0, 0))
            month_frame.grid(row=row, column=col, padx=10, pady=10)
            month_frame.grid_propagate(False)

            # month name as a button
            # TODO: clicking one of these should open a month view for that month
            month_name = calendar.month_name[month]
            month_button = ttk.Button(month_frame, text=month_name)
            month_button.grid(row=0, column=0, columnspan=7, pady=(0, 15))

            # under the month name there should be the weekdays (abbreviated so they
            # don't take too much space)
            for day_name in calendar.day_name:
                day_label = ttk.Label(month_frame, text=day_name[:3], width=4)
                day_label.grid(row=1, column=list(calendar.day_name).index(day_name), pady=(0, 5))

            # under the abbreviated weekdays there should be a grid of days numbered from
            # 1 to 28-31, depending on how many days the month has; the calendar module
            # gives days outside the given month as "0", which can be ignored
            # label instead of button seems necessary here for style reasons and for properly fitting on the grid
            for week in month_calendar:
                for day in week:
                    if day > 0:
                        if datetime.date(self._current_year, month, day)== datetime.date.today():
                            day_label = ttk.Label(month_frame, text=str(day), cursor="hand2", width=-2, background='yellow')
                        else:
                            day_label = ttk.Label(month_frame, text=str(day), cursor="hand2", width=-2)
                        # the user should be able to click any given day to see, add or delete notes
                        # TODO: actually implement that, currently just prints the date for testing
                        day_label.grid(row=month_calendar.index(week) + 2, column=week.index(day))
                        day_label.bind("<Button-1>", lambda event, d=day, m=month, y=self._current_year: self.print_date_test(d, m, y))

            col += 1
            if col == 3:
                col = 0
                row += 1

    def _init(self):
        # frame for menus (configure, add/remove notes, help, logout)
        self._menu_frame = ttk.Frame(self._root)
        self._menu_frame.pack(anchor=constants.NW)

        # main container frame
        self._main_frame = ttk.Frame(self._root)
        self._main_frame.pack(fill=constants.NONE, expand=True)
        
        # frame that contains buttons like so: < {year} >
        # for going forward or back in time
        self._year_menu_frame = ttk.Frame(self._main_frame)
        self._year_menu_frame.pack()

        # frame that contains the calendar itself
        self._calendar_frame = ttk.Frame(self._main_frame)
        self._calendar_frame.pack()

        self._display_menu()
        self._display_year_menu(self._current_year)
        self._display_months()

    def print_date_test(self, day, month, year):
        print(f"day: {day} month: {month} year: {year}")