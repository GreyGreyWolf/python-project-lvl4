install:
	poetry install

lint:
	poetry run flake8 task_manager/

test:
	poetry run purest --cov-report=xml --cov=task_manager tests/