from .settings import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['*']


# Add whitenoise module for production for handling staticfiles
MIDDLEWARE += [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Database
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

