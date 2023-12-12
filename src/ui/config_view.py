from tkinter import ttk
from services.config_service import config_service


class ConfigView:

    def __init__(self, state, root, calendar_view):
        self._state = state

        self._root = root
        self._root.title("Config")

        self._user = self._state.get_current_user()

        self._show_calendar_view = calendar_view

        self._menu_frame = None
        self._config_frame = None

        self._init()

    def pack(self):
        self._menu_frame.pack()
        self._config_frame.pack()

    def destroy(self):
        self._menu_frame.destroy()
        self._config_frame.destroy()

    def _display_menu(self):
        buttons = {}
        buttons["back"] = ttk.Button(
            self._menu_frame, text="back", padding=5, cursor="hand2")
        buttons["back"].grid(row=0, column=0, padx=5, pady=10)
        buttons["back"].bind(
            "<Button-1>", lambda event: self._handle_back_button())

    def _init_config_buttons(self):
        user_settings = config_service.get_user_config(self._user)
        single_user_button_text = user_settings.settings["single_user"]

        single_user_label = ttk.Label(
            self._config_frame, text="enable single user mode")
        single_user_label.grid(row=0, column=0)

        single_user_button = ttk.Button(self._config_frame, text=single_user_button_text,
                                        command=lambda: self._handle_set_single_user(single_user_button_text))
        single_user_button.grid(row=0, column=1)

    def _handle_set_single_user(self, value):
        config_service.clear_single_user()

        if value == "off":
            config_service.set_single_user(self._user, "on")

        self._init_config_buttons()

    def _handle_back_button(self):
        self._show_calendar_view()

    def _init(self):

        self._menu_frame = ttk.Frame(self._root, padding=10)
        self._config_frame = ttk.Frame(self._root, padding=10)

        self._display_menu()

        self._init_config_buttons()
