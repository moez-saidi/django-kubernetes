import os
from pathlib import Path

import environ

from .base import (  # noqa: F401
    AUTH_PASSWORD_VALIDATORS,
    DEFAULT_AUTO_FIELD,
    INSTALLED_APPS,
    LANGUAGE_CODE,
    MIDDLEWARE,
    ROOT_URLCONF,
    STATIC_URL,
    TEMPLATES,
    TIME_ZONE,
    USE_I18N,
    USE_L10N,
    USE_TZ,
    WSGI_APPLICATION,
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'env', 'backend.env'))


# Convert str to boolean
def str_to_bool(s):
    return s.lower() in ('true', '1', 't')


SECRET_KEY = env('SECRET_KEY')

DEBUG = str_to_bool(env('DEBUG'))

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
