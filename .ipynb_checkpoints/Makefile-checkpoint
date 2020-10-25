install:
	poetry install

lint:
	poetry run flake8 task_manager/

test:
	poetry run pytest --cov-report=xml --cov=tasks tests.py

runserver:
	poetry run python3 manage.py runserver

runshell:
	poetry run python3 manage.py shell

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

build:
	poetry build
