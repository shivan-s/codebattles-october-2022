#!/bin/sh
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn --worker-tmp-dir /dev/shm config.wsgi -b 0.0.0.0:8000
