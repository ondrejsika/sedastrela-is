import os


def _env(variable, default=None):
    return os.environ.get(variable, default)


def _env_bool(variable, default=None):
    if _env(variable, default) == 'true':
        return True
    elif _env(variable, default) == 'false':
        return False
    else:
        return default


def _env_int(variable, default=None):
    return int(_env(variable, default))


ENVIRONMENT = _env('ENVIRONMENT')

if not ENVIRONMENT:
    raise Exception('No environment selected')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '@)#)^e@-66*e9+m#srm)c3)0)4*o)y=#0@$wt6wis6wt@glx2@'

DEBUG = _env_bool('DEBUG', False)


ALLOWED_HOSTS = _env('ALLOWED_HOSTS').split() if _env('ALLOWED_HOSTS') else []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mailing',

    'sedastrela_is.person',
    'sedastrela_is.event',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': _env('DATABASE_ENGINE'),
        'NAME': _env('DATABASE_NAME'),
        'USER': _env('DATABASE_USER'),
        'PASSWORD': _env('DATABASE_PASSWORD'),
        'HOST': _env('DATABASE_HOST'),
        'PORT': _env('DATABASE_PORT'),
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')

EMAIL_HOST = _env('EMAIL_HOST', 'localhost')
EMAIL_PORT = _env_int('EMAIL_PORT', 25)
EMAIL_HOST_USER = _env('EMAIL_USER')
EMAIL_HOST_PASSWORD = _env('EMAIL_PASSWORD')
EMAIL_USE_TLS = _env_bool('EMAIL_USE_TLS')

DEFAULT_EMAIL_FROM = _env('DEFAULT_EMAIL_FROM')
assert DEFAULT_EMAIL_FROM

SITE_URL = _env('SITE_URL')
assert SITE_URL
SITE_URL_FULL = _env('SITE_URL_FULL')
assert SITE_URL_FULL

ADMIN_NOTIFICATION_EMAILS = _env('ADMIN_NOTIFICATION_EMAILS').split()
assert ADMIN_NOTIFICATION_EMAILS
