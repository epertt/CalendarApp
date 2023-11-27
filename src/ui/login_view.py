from tkinter import ttk, constants
from services.calendar_service import calendar_service, InvalidCredentialsError, UserExistsError


class LoginView:

    def __init__(self, root, calendar_view, menu_buttons=None):
        self._root = root
        self._root.title("Login")

        self._show_calendar_view = calendar_view

        self._menu_buttons = menu_buttons

        self._login_frame = None

        self.account_created_label1 = None
        self.account_created_label2 = None

        self._username_field = None
        self._password_field = None
        self._login_button = None

        self._init()

    def pack(self):
        self._login_frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._login_frame.destroy()

    def _init_help_message(self,
                           text1="enter username and password to log in",
                           text2="account will be created if it doesn't exist"
                           ):
        if self.account_created_label1 or self.account_created_label2:
            self.account_created_label1.destroy()
            self.account_created_label2.destroy()

        self.account_created_label1 = ttk.Label(
            self._login_frame, text=text1, justify=constants.CENTER)
        self.account_created_label2 = ttk.Label(
            self._login_frame, text=text2, justify=constants.CENTER)
        self.account_created_label1.grid(
            row=0, column=0, columnspan=3, sticky=constants.W)
        self.account_created_label2.grid(
            row=1, column=0, columnspan=3, sticky=constants.W)

    def _init_labels(self):
        username_label = ttk.Label(self._login_frame, text="username")
        password_label = ttk.Label(self._login_frame, text="password")
        username_label.grid(row=2, column=0, columnspan=1, sticky=constants.W)
        password_label.grid(row=3, column=0, columnspan=1, sticky=constants.W)

    def _init_fields(self):
        self._username_field = ttk.Entry(
            self._login_frame, justify=constants.CENTER)
        self._password_field = ttk.Entry(
            self._login_frame, show="*", justify=constants.CENTER)
        self._username_field.grid(
            row=2, column=1, pady=5, columnspan=2, sticky=constants.W)
        self._password_field.grid(
            row=3, column=1, pady=5, columnspan=2, sticky=constants.W)

    def _init_buttons(self):
        login_button = ttk.Button(
            self._login_frame, text="login", command=lambda: self._handle_login())
        login_button.grid(row=4, column=0, columnspan=3,
                          pady=5, sticky=(constants.W, constants.E))

    def _init(self):
        calendar_service.logout()
        if self._menu_buttons:
            self._menu_buttons.destroy()

        self._login_frame = ttk.Frame(self._root)

        self._init_help_message()
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
            self._init_help_message("", "the password is incorrect")
            try:
                calendar_service.add_user(username, password)
                self._init_help_message(
                    f"created account with user {username}", "click login again to log in")
            except UserExistsError:
                self._init_help_message(
                    "a user with that name exists,", "but the password is incorrect")
