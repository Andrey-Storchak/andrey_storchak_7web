import os

from .common import *

import dj_database_url

DEBUG = True
DATABASES = {'default': dj_database_url.config()}

STATIC_ROOT = 'static/'
STATICFILES_DIRS = (
    )
