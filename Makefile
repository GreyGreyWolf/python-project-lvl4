install:
	poetry install

lint:
	poetry run flake8 task_manager/

test:
	poetry run --source='.' manage.py test
	coverage report
	coverage xml

runserver:
	poetry run python3 manage.py runserver

runshell:
	poetry run python3 manage.py shell

build:
	poetry build
