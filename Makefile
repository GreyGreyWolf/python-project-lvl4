install:
	@poetry install

docker-install:
	docker-compose run django sh -c "make install"

.env:
	@test ! -f .env && cp .env.example .env

makemigrations:
	@poetry run python manage.py makemigrations

docker-makemigrations:
	docker-compose run django sh -c "make makemigrations"

migrate:
	@poetry run python manage.py migrate

docker-migrate:
	docker-compose run django sh -c "make migrate"

production-migrate:
	heroku run python manage.py migrate

start: migrate
	@poetry run python manage.py runserver 0.0.0.0:8000

docker-start:
	docker-compose up

setup: migrate
	@poetry run python manage.py createsuperuser

docker-setup:
	docker-compose run django sh -c "make setup"

shell:
	@poetry run python manage.py shell

docker-shell:
	docker-compose run django sh -c "make shell"

lint:
	@poetry run flake8 config

test:
	@poetry run python manage.py test

docker-test:
	docker-compose run django sh -c "make test"

check: lint test

coverage:
	@poetry run coverage run --source='.' manage.py test
	@poetry run coverage xml