import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'xjf^@5ha&mi1%e2bojksl+_8057rbh(b0mio7fc&ypz=5@p#q_'

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.pynote',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'andrey_storchak_test_7web.urls'

WSGI_APPLICATION = 'andrey_storchak_test_7web.wsgi.application'


import dj_database_url

DATABASES = {'default': dj_database_url.config()}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
     'templates/',
     'templates/pynote/templates/'
)


STATIC_URL = '/static/'

STATIC_ROOT = 'static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)