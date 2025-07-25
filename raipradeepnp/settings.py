# settings.py
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()  
import os
from django.contrib.messages import constants as messages
ROOT_URLCONF = 'raipradeepnp.urls'
DEBUG = True  # or already set
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'k!7%h&@5+_nxy9k@jv-#n1o&8v#by0g(e^@12v-=34l%2mrq&j'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'hcaptcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'website' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# No need to add app static folders here unless you have a global static dir
STATICFILES_DIRS = []  # Or leave it out


# Use WhiteNoise in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'website' / 'static']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# Add your reCAPTCHA v3 keys from https://www.google.com/recaptcha/admin
#RECAPTCHA_PUBLIC_KEY = '6LewQIcrAAAAAETOqSrULrA96cXX4plKT0_nnY7R'
#RECAPTCHA_PRIVATE_KEY = '6LewQIcrAAAAAFGdnhYmTuAFxkUbSmfg6QY-jFh8'
#RECAPTCHA_DEFAULT_ACTION = 'generic'
#RECAPTCHA_REQUIRED_SCORE = 0.5  # Adjust threshold as needed

# Optional for reCAPTCHA v3 (if using score)
#RECAPTCHA_DEFAULT_ACTION = 'contact_form'

HCAPTCHA_SITEKEY = '88a6c2a8-412a-4714-9fc2-ffa48a5cab9c'
HCAPTCHA_SECRET = 'ES_54b8ca2551e845e99a015ce016b96c46'


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
