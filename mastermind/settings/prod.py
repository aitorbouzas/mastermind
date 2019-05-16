from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.getenv('DATABASE_NAME', 'django'),
        'USER': os.getenv('DATABASE_USER', 'django'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'django'),
        'HOST': os.getenv('DATABASE_SERVICE_HOST', 'database'),
        'PORT': os.getenv('DATABASE_SERVICE_PORT', 5432)
    }
}
