import os
from pathlib import Path

import environ

from .base import (  # noqa: F401
    API_PREFIX,
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


ENV = env('ENV')

INSTALLED_APPS += [
    'drf_spectacular',
]

SECRET_KEY = env('SECRET_KEY')

DEBUG = str_to_bool(env('DEBUG'))

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Django Kubernetes Playground',
    'DESCRIPTION': '''
       django-kubernetes is a platform that will deploy containerized applications across
       multiple hosts. It provides basic mechanisms for deployment, maintenance, and scaling
       of applications using the power of kubernetes under the hood.
    ''',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
