#!/bin/sh

echo 'Running collecstatic...'
#python manage.py collectstatic --no-input --settings=config.settings.production

echo 'Applying migrations...'
#python manage.py wait_for_db --settings=config.settings.production
python manage.py migrate

echo 'Running server...'
#gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.production config.wsgi:application --bind 0.0.0.0:$PORT
python manage.py iniciar_user
python manage.py runserver 0.0.0.0:$PORT