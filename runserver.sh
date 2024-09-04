#!/bin/bash

source /venv/bin/activate

# sleep 5
# python manage.py makemigrations
# python manage.py migrate

python manage.py runserver 0.0.0.0:8000
# gunicorn --env DJANGO_SETTINGS_MODULE=calculator.settings calculator.wsgi:application authbind -b 0.0.0.0:8000 --log-level debug -w 2 -t 500