#!/bin/bash

case "$PROCESS" in
"DEV_DJANGO")   
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py collectstatic --noinput &&
    python manage.py makemigrations &&
    python manage.py migrate &&
    python manage.py initadmin &&
    uvicorn config.asgi:application --reload-dir apps --debug --host 0.0.0.0 --port 8000 --log-level info --use-colors
    ;;
"DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py collectstatic --noinput &&
    python manage.py makemigrations &&
    python manage.py migrate &&
    python manage.py initadmin &&
    gunicorn --config gunicorn.conf.py config.wsgi:application --reload --capture-output --log-level info --access-logfile -
    ;;
esac