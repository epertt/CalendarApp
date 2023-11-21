# CalendarApp
Simple multi-user calendar application that shows a single year, month or week, with the current day highlighted. Other (not yet implemented) features will include adding notes to days, as well as editing the notes, which will be shown on the calendar view.

## Documentation
- [Requirements specification](./dokumentaatio/requirements_specification.md)
- [Time tracking](./dokumentaatio/time_tracking.md)
- [Changelog](./dokumentaatio/changelog.md)

## Installation
Requirements:
- Python>=3.8
- Poetry

Clone the git repository and run the following commands on your terminal:
```
poetry install
poetry run invoke start
```

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