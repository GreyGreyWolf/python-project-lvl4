install:
		poetry install

lint:
		poetry run flake8 \
			--exclude .git,__pycache__,migrations,staticfiles
migrate:
		poetry run python manage.py migrate

start: migrate
		poetry run python manage.py runserver 0.0.0.0:8000

docker-start:
		docker-compose up

setup: migrate
		poetry run python manage.py createsuperuser

docker-setup:
		docker-compose run django sh -c "make setup"

shell:
		poetry run python manage.py shell

docker-shell:
		docker-compose run django sh -c "make shell"

test:
		coverage run --source='.' manage.py test
		coverage report
		coverage xml

docker-test:
	docker-compose run django sh -c "make test"
