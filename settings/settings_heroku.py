from .settings import *
import dj_database_url

DEBUG=False
DATABASES = {'default': dj_database_url.config()}
ADMIN_MEDIA_PREFIX = 'https://github.com/django/django/tree/master/django/contrib/admin/static/'