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

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


# Convert str to boolean
def str_to_bool(s):
    return s.lower() in ('true', '1', 't')


SECRET_KEY = env('SECRET_KEY')

DEBUG = str_to_bool(env('DEBUG'))

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('PGPORT'),
        'ATOMIC_REQUESTS': True,
    }
}
