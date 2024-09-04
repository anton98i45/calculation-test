#!/bin/bash

source /venv/bin/activate

python manage.py makemigrations
python manage.py migrate

gunicorn --env DJANGO_SETTINGS_MODULE=calculator.settings calculator.wsgi:application authbind -b 0.0.0.0:8000 --log-level debug -w 2 -t 500