import os

from .common import *

import dj_database_url

DEBUG = False
DATABASES = {'default': dj_database_url.config()}

STATIC_ROOT = ''
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
    os.path.join(PROJECT_ROOT, 'static/admin'),
    )
