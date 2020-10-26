install:
        poetry install

lint:
	    poetry run flake8 \
		    --exclude .git,__pycache__,migrations,staticfiles

test:
        coverage run --source='.' manage.py test
        coverage report
        coverage xml

runserver:
        poetry run python3 manage.py runserver

runshell:
	    poetry run python3 manage.py shell

migrate:
        poetry run python3 manage.py makemigrations
        poetry run python3 manage.py migrate
