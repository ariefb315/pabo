#!/bin/sh

set -e

python manage.py collectstatic --noinput

# --noinput

uwsgi --socket :8000 --master --enable-threads --module pabo.wsgi