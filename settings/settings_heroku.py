import os

import dj_database_url

from .settings import *

DEBUG = False

DATABASES = {'default': dj_database_url.config()}

ALLOWED_HOSTS = ['*']
STATIC_ROOT=os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'admin'),
)