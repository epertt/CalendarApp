from tkinter import ttk, constants


class HelpView:

    def __init__(self, state, root, calendar_view):
        self._state = state

        self._root = root
        self._root.title("Help")

        self._show_calendar_view = calendar_view

        self._menu_frame = None
        self._help_frame = None

        self._init()

    def pack(self):
        self._menu_frame.pack()
        self._help_frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._menu_frame.destroy()
        self._help_frame.destroy()

    def _display_menu(self):
        buttons = {}
        buttons["back"] = ttk.Button(
            self._menu_frame, text="back", padding=5, cursor="hand2")
        buttons["back"].grid(row=0, column=0, padx=5, pady=10)
        buttons["back"].bind(
            "<Button-1>", lambda event: self._handle_back_button())

    def _init_help_labels(self, help_messages):
        for i, message in enumerate(help_messages):
            help_label = ttk.Label(self._help_frame, text=message)
            help_label.grid(row=i, column=0)

    def _handle_back_button(self):
        self._show_calendar_view()

    def _init(self):

        self._menu_frame = ttk.Frame(self._root, padding=10)
        self._help_frame = ttk.Frame(self._root, padding=10)

        self._display_menu()

        self._init_help_labels([
            "Click on days to open date view where you can add and remove notes",
            "Click on months to open month view instead of the default year view",
            "Current day is highlighted on year and month views",
            "Work in progress features:",
            "Month view",
            "(Fairly limited) configuration (will be) available in configuration menu",
            "Showing days with notes on the year or month views"
        ])
