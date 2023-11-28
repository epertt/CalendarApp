from tkinter import Tk
from ui.ui import UI


def main():
    root_window = Tk()
    root_window.resizable(False, False)
    root_window.title("CalendarApp")

    ui_view = UI(root_window)
    ui_view.start()

    root_window.mainloop()


if __name__ == "__main__":
    main()
