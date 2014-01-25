#web: DJANGO_SETTINGS_MODULE=settings.settings_heroku python manage.py runserver "0.0.0.0:$PORT" 
web: DJANGO_SETTINGS_MODULE=settings.settings_heroku gunicorn --workers=1 --bind=0.0.0.0:8000 app:application
