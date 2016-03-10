import os

import settings_local


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '@)#)^e@-66*e9+m#srm)c3)0)4*o)y=#0@$wt6wis6wt@glx2@'

DEBUG = True

ALLOWED_HOSTS = []


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
        'ENGINE': settings_local.DATABASES_ENGINE,
        'NAME': settings_local.DATABASES_NAME,
        'USER': settings_local.DATABASES_USER,
        'PASSWORD': settings_local.DATABASES_PASSWORD,
        'HOST': settings_local.DATABASES_HOST,
        'PORT': settings_local.DATABASES_PORT,
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')

EMAIL_HOST = settings_local.EMAIL_HOST
EMAIL_PORT = settings_local.EMAIL_PORT
EMAIL_HOST_USER = settings_local.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = settings_local.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = settings_local.EMAIL_USE_TLS

DEFAULT_EMAIL_FROM = settings_local.DEFAULT_EMAIL_FROM

