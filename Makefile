install:
		poetry install

lint:
		poetry run flake8 \
			--exclude .git,__pycache__,migrations,staticfiles
migrate:
		poetry run python manage.py migrate

start: migrate
		poetry run python manage.py runserver 0.0.0.0:8000

setup: migrate
		poetry run python manage.py createsuperuser

shell:
		poetry run python manage.py shell

test:
		coverage run --source='.' manage.py test
		coverage report
		coverage xml
