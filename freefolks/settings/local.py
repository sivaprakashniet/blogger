"""
This is an example settings/local.py file.
These settings overrides what's in settings/base.py
"""

from . import base


# To extend any settings from settings/base.py here's an example.
# If you don't need to extend any settings from base.py, you do not need
# to import base above
INSTALLED_APPS = base.INSTALLED_APPS + ('django_nose',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fin',
        'USER': 'root',
        'PASSWORD': 'nymeria@1991',
        'HOST': '',
        'PORT': '',
        #'OPTIONS': {
        #    'init_command': 'SET storage_engine=InnoDB',
        #    'charset' : 'utf8',
        #    'use_unicode' : True,
        #},
        #'TEST_CHARSET': 'utf8',
        #'TEST_COLLATION': 'utf8_general_ci',
    },
    # 'slave': {
    #     ...
    # },
}

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control. Consider loading
# the secret key from an environment variable or a file instead.
SECRET_KEY = '^d*_qj2d!=jfe0u+4_m#l+#oshkhuhcdt=j(a2me=#n31maa(8'

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'django'
# BROKER_PASSWORD = 'django'
# BROKER_VHOST = 'django'
# CELERY_RESULT_BACKEND = 'amqp'

## Log settings


#Admin customization
GRAPPELLI_ADMIN_TITLE = 'FreeFolks'

# Remove this configuration variable to use your custom logging configuration
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'loggers': {
        'freefolks': {
            'level': "DEBUG"
        }
    }
}

INTERNAL_IPS = ('127.0.0.1')

APP_CONSTANTS = {
    'FIELDS':[{'key':'bank', 'value':'Bank'},{'key':'transaction_type', 'value':'Transaction Type'}]
}

ACCOUNT_LOGOUT_ON_GET = True
LOGIN_REDIRECT_URL = '/blog'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_UNIQUE_EMAIL = True


TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 30,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True



