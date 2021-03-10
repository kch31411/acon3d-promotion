#!/bin/bash

python manage.py migrate
python manage.py loaddata initial-data.yaml
python manage.py runserver 0:8000

exec "$@"
