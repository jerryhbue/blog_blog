from .base import * #NOQA

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}