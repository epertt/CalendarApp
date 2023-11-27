# CalendarApp
Simple multi-user calendar application that shows a single year, month or week, with the current day highlighted. Other (not yet implemented) features will include adding notes to days, as well as editing the notes, which will be shown on the calendar view.

## Documentation
- [Requirements specification](./dokumentaatio/requirements_specification.md)
- [Time tracking](./dokumentaatio/time_tracking.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Software architecture](./dokumentaatio/arkkitehtuuri.md)
- [Known issues](./dokumentaatio/known_issues.md)

## Installation
Requirements:
- Python>=3.8
- Poetry (tested on 1.7.0)

Clone the git repository and run the following commands on your terminal:
```
poetry install
poetry run invoke setup
poetry run invoke start
```
If you get an error while running ```poetry install```, your poetry installation is probably out of date. If on linux, update to a newer version using your distribution's package manager, or run the following to install poetry:
```
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
```

If you get an error starting the program, you probably forgot to run ```poetry run invoke setup```

## Testing:
Running tests:
```
poetry run invoke test
```
Generating test coverage:
```
poetry run invoke coverage-report:
```
Generating test coverage and displaying it in the browser:
```
poetry run invoke display-coverage-report
```
