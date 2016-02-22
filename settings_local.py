import os
_BASE_DIR = os.path.dirname(__file__)

DATABASES_ENGINE = 'django.db.backends.sqlite3'
DATABASES_NAME = os.path.join(_BASE_DIR, 'db.sqlite3')
DATABASES_USER = None
DATABASES_PASSWORD = None
DATABASES_HOST = None
DATABASES_PORT = None


EMAIL_HOST = 'smtp.seznam.cz'
EMAIL_HOST_USER = 'ondrej-smtp-1@seznam.cz'
EMAIL_HOST_PASSWORD = 'asdfasdf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


DEFAULT_EMAIL_FROM = EMAIL_HOST_USER
DEFAULT_EMAIL_FROM = 'info@sedastrela.cz'
