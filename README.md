# Do you have what it takes to be a Maverick?

Application: coding-tester

Idea: Create a site that can be used in a Mavericks recruitement process to check whether the applicant has "what it takes to be a Maverick". There are multiple tests available that can be given to the applicant. The desired test can be selected with URL-parameters. New Tests can easily be added. The applicant needs to submit an URL to his/her API endpoint and when submitted, should the application test whtether or not it's implemented properly. The application responds with error messages or with a form that can be fullfilled if the test was successfull.

## Mavericks Hackathon 2021-10-08

The application is created in Mavericks Hackathon 2021 (2021-10-08 - 2021-10-09). Timeframe was 24h!

Project team: Niko Lindroos and Jussi Pölkki.

## Backend

A service that makes randomised tests against services to see whether they implement a given endpoint correctly (for checking coding assignments)

A fork from City of Helsinki coding-assignment-tester -repo (https://github.com/City-of-Helsinki/coding-assignment-tester), but much refactored.

The plan was to study how well a Mongo DB database can operate with default Django configuration. It was also planned that the user could login with a social auth, but the timeframe ended and mongo and social auth were disbanded. A SQL Lite was used instead.

What has changed from original fork:

- The views can respond with JSON responses.
- Tests are refactored to their own files.
- More information is requested from the applicant when a successfull answer is given. This included the applicant name, phone number, favored tech and work expirement.
- Admin views much improved.

## Frontend

Created with Vue 3. The plan was to study new version of Vue. Mavericks colors and fonts used as a theme.

## How to run

Via Docker: `docker-compose up` in a root of the project. This launches the backend in port 8000 and the frontend in the port 3000.

Development server of the backend: In a backend -folder, run the following:

- `pip install -r requirements-dev.txt` and `pip install -r requirements.txt`. Preferred way to maintain dependencies is with pip-tools (`pip-compile` and `pip-sync requirements.txt requirements-dev.txt`)
- `python manage.py migrate` to migrate the database scheme.
- `python manage.py createsuperuser` to create an admin user. Admin site in `localhost:8000/admin`.
- `python runserver`

Development server of the frontend: In a frontend -folder, run `npm run install` and `npm run dev`.

## How to add a new test

In backend -project settings, there is a TEST_ASSIGNMENTS setting, which is a dictionary where the key is the name of the test (used in url) and value is the tester function.

Example:

```python
TEST_ASSIGNMENTS = {
    "sananmuunnos": generate_swaps,
    "fibonacci": generate_fibo,
    "flatten": generate_flatten,
    "zerodepth": generate_zero_trees,
}
```

The tests are listed in directory `/backend/test_assignments/`.
