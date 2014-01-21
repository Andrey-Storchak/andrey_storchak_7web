BASE=`pwd`
LIB=$(BASE)/lib
SETTINGS=$(BASE)/settings
APPS=$(BASE)/apps
PYTHONPATH=$(BASE):$(LIB):$(APPS):$(SETTINGS)
SETTINGS_LOCAL=settings.settings_local
SETTINGS_HEROKU=settings.settings_heroku
MANAGE=$(BASE)/manage.py

init:
	pip install -r requirements.txt
	DJANGO_SETTINGS_MODULE=$(SETTINGS_LOCAL) $(MANAGE) syncdb --noinput
	$(MANAGE) loaddata db_data.json

