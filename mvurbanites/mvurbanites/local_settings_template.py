from os.path import join, normpath

DEBUG = False
TEMPLATE_DEBUG = DEBUG
PRODUCTION = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

ALLOWED_HOSTS = ['mvurbanites.com', 'www.mvurbanites.com']

# API key for meetup.com
MEETUP_KEY = ''

EMAIL_HOST = "localhost"
EMAIL_PORT = "25"

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
