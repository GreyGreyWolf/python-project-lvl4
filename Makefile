install:
        python poetry install
lint:
        python poetry run flake8
test:
        python poetry run coverage run --source='.' --omit '.venv/*' manage.py test
        python poetry run coverage report
        python poetry run coverage xml

run:
        python poetry run python manage.py runserver

requirements:
        python poetry export -f requirements.txt -o requirements.txt
