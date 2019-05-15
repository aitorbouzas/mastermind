from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mastermind',
        'USER': 'postgres',
        'PASSWORD': 'abc1234.',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
