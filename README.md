# python-project-lvl4

# Task manager

<a href="https://codeclimate.com/github/GreyGreyWolf/python-project-lvl4/maintainability"><img src="https://api.codeclimate.com/v1/badges/f7663e070e5c463316e7/maintainability" /></a>
<a href="https://codeclimate.com/github/GreyGreyWolf/python-project-lvl4/test_coverage"><img src="https://api.codeclimate.com/v1/badges/f7663e070e5c463316e7/test_coverage" /></a>
[![Build Status](https://travis-ci.com/GreyGreyWolf/python-project-lvl4.svg?branch=master)](https://travis-ci.com/GreyGreyWolf/python-project-lvl4)

# About this program

This app is simple task manager.

# Getting started

You should rename file .env.example to .env and added value of variable environments
```
DATABASE_URL = !Path to your database!
DEBUG = !'True' if you want to use debug mode!
SECRET_KEY = !Key for Django settings!
POST_SERVER_ITEM_ACCESS_TOKEN = !Token for your rollbar account!
```

After this:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py creatsuperuser
```

For start application:

```
python3 manage.py runserver
```

The application is locally available at [http://127.0.0.1:8000]

# Usage example

You can watch it at work here: https://greywolf-task-manager.herokuapp.com/

