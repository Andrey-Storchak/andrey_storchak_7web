import os

from .common import *

import dj_database_url

DEBUG = False
DATABASES = {'default': dj_database_url.config()}

STATIC_ROOT = os.path.join(BASE_DIR,'static/')
STATIC_URL = '/static/'

