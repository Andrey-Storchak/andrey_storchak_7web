import os

from .common import *

import dj_database_url

DEBUG = False
DATABASES = {'default': dj_database_url.config()}

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
