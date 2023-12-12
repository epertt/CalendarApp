#### 1. Download the latest release
The latest release is available ["here"](https://github.com/epertt/CalendarApp/releases/latest)

#### 2. Ensure you have the dependencies
The program has been tested to work on
- A version of python newer than 3.8
- Version 1.7.0 of python-poetry

#### 3. Run the following commands
1. Installing the dependencies:
```
poetry install
```
2. Setting up the database:
```
poetry run invoke setup
```
3. Starting the program:
```
poetry run invoke start
```

#### 3.5 If you get an error while running the install or start commands
If you get an error while running ```poetry install```, your poetry installation is probably out of date. If on linux, update to a newer version using your distribution's package manager, or run the following to install poetry:
```
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
```
If you get an error starting the program, you probably forgot to run ```poetry run invoke setup```

#### 4. Creating an account and logging in
- There is no separate page for creating an account. You can type in any name and password, and the program will create an account with that name and password if one does not already exist
- You have to press login twice when you are first creating an account
- If you select the "single user mode" option in the configuration view, you don't have to log in the next time you open the program

#### 5. Adding notes and navigating the calendar
- You can click on any day to open a date view where you can add or remove notes for the selected day. You can navigate between days, months and years in the various view by pressing the "<" and ">" buttons
- You can click the help button to see some tips about using the program
- You can change users by logging out, but doing so will also turn off the single user mode