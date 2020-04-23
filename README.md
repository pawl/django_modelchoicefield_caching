In this repository, I try to figure out the best way to cache ModelChoiceField's `queryset`.

## Installation

1. Clone this repository and navigate to the directory.
1. Create virtualenv: `virtualenv .venv`
1. Activate the virtualenv: `source .venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Initialize database schema: `python manage.py migrate`
1. Load initial data: `python manage.py loaddata myapp/fixtures/*`

## Usage

Start the back-end in your first terminal:
`python manage.py runserver`

Run this command to POST json to the api:
`curl http://localhost:8000/`

Watch the terminal for results.
