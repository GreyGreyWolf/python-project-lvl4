install:
		poetry install
lint:
		poetry run flake8 \
			   --exclude .git,__pycache__,migrations,staticfiles
test:
		poetry run coverage run --source='.'  manage.py test
		poetry run coverage report
		poetry run coverage xml

run:
		poetry run python manage.py runserver
