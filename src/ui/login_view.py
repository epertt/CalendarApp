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
        account_created_label1 = ttk.Label(self._login_frame, text="enter username and password to log in")
        account_created_label2 = ttk.Label(self._login_frame, text="account will be created if it doesn't exist")
        username_label = ttk.Label(self._login_frame, text="username")
        password_label = ttk.Label(self._login_frame, text="password")
        account_created_label1.grid(row=0, column=0, columnspan=3, sticky=constants.W)
        account_created_label2.grid(row=1, column=0, columnspan=3, sticky=constants.W)
        username_label.grid(row=2, column=0, columnspan=1, sticky=constants.W)
        password_label.grid(row=3, column=0, columnspan=1, sticky=constants.W)
        

    def _init_fields(self):
        self._username_field = ttk.Entry(self._login_frame, justify=constants.CENTER)
        self._password_field = ttk.Entry(self._login_frame, show="*", justify=constants.CENTER)
        self._username_field.grid(row=2, column=1, pady=5, columnspan=2, sticky=constants.W)
        self._password_field.grid(row=3, column=1, pady=5, columnspan=2, sticky=constants.W)

    def _init_buttons(self):
        self.login_button = ttk.Button(self._login_frame, text="login", command=lambda: self._handle_login())
        self.login_button.grid(row=4, column=0, columnspan=3, pady=5, sticky=(constants.W, constants.E))
        #self.login_button.grid_columnconfigure(1, weight=1)

    def _init(self):
        calendar_service.logout()

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
            if calendar_service.create_user(username, password):
                print(f"created account with user {username}")
            else:
                print(f"account with username {username} already exists")
