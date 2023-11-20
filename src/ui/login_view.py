from tkinter import ttk, constants
from services.calendar_service import calendar_service, InvalidCredentialsError

class LoginView:

    def __init__(self, root, calendar_view):
        self._root = root
        self._root.title("Login")

        self._show_calendar_view = calendar_view

        self._login_frame = None

        self._username_field = None
        self._password_field = None
        self._login_button = None

        self._init()

    def pack(self):
        self._login_frame.pack(fill=constants.NONE, expand=True)

    def destroy(self):
        self._login_frame.destroy()

    def _init_labels(self):
        username_label = ttk.Label(self._login_frame, text="username")
        password_label = ttk.Label(self._login_frame, text="password")
        username_label.grid(row=0, column=0, columnspan=1, sticky=constants.W)
        password_label.grid(row=1, column=0, columnspan=1, sticky=constants.W)

    def _init_fields(self):
        self._username_field = ttk.Entry(self._login_frame)
        self._password_field = ttk.Entry(self._login_frame)
        self._username_field.grid(row=0, column=1, pady=5, padx=5, columnspan=2, sticky=constants.E)
        self._password_field.grid(row=1, column=1, pady=5, padx=5, columnspan=2, sticky=constants.E)

    def _init_buttons(self):
        self.login_button = ttk.Button(self._login_frame, text="login", command=lambda: self._handle_login())
        self.login_button.grid(row=2, column=0, columnspan=3, pady=5, sticky=(constants.W, constants.E))
        self.login_button.grid_columnconfigure(1, weight=1)

    def _init(self):
        self._login_frame = ttk.Frame(self._root)

        self._init_labels()
        self._init_fields()
        self._init_buttons()

        self._login_frame.columnconfigure(0, weight=1)

    def _handle_login(self):
        username = self._username_field.get()
        password = self._password_field.get()

        try:
            calendar_service.login(username, password)
            self._show_calendar_view()
        except InvalidCredentialsError:
            print("ruh roh: _handle_login @ login_view.py")
