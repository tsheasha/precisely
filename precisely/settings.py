# Django settings for precisely project.
import dj_database_url
import os
from hellosign_sdk import HSClient

gettext = lambda s: s

PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Tarek Sheasha', 'tarek@skillacademy.com')
)

MANAGERS = ADMINS

DEPLOYED_ADDRESS = "http://precisely.herokuapp.com"

if 'DATABASE_URL' in os.environ:
    DEPLOYED_ADDRESS = "http://precisely.herokuapp.com"
    DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'precisely_db',
            'USER': '', 
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join( PROJECT_DIR, 'media/')

MEDIA_URL = '/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'z6byeu%cheby^mt0xie=qflfi71^5_&amp;8my#gbr+*!9!o^llddc'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'precisely.urls'

WSGI_APPLICATION = 'precisely.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join( os.path.dirname( __file__ ), 'templates' ),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'sign_pdf',
    'gunicorn',
    
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

HELLO_SIGN_API_KEY = "89667cac45af1d324626e112f2bf3150a1fe61241900b733f4927cdf5dfda831"
client = HSClient(api_key=HELLO_SIGN_API_KEY)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
