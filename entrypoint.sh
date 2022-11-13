#!/bin/sh

set -e

python ./manage.py collectstatic --no-input
python ./manage.py migrate

gunicorn --env DJANGO_SETTINGS_MODULE=config.local -b 0.0.0.0:8000 coupon_manager.wsgi