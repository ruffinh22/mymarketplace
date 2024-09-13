from pathlib import Path
from decouple import config

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-ep*law!)5vaj@kza@dx47b$ye%@8csy=j@+j%+jw(9^v_jg#)l'
DEBUG = True
ALLOWED_HOSTS = []

# Custom user model and authentication backends
AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth authentication
]

# Site ID for Django Allauth
SITE_ID = 1

# Login and logout redirection URLs
LOGIN_REDIRECT_URL = 'dashboard'  # Redirection after login
LOGOUT_REDIRECT_URL = 'account_login'  # Redirection after logout

# Installed apps including Django Allauth and its providers
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for Django Allauth
    'allauth',  # Django Allauth base app
    'allauth.account',  # Allauth account management
    'allauth.socialaccount',  # Social accounts support
    'allauth.socialaccount.providers.google',  # Google provider
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'users',  # Your custom user app
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # This middleware should be at the end
]

# URL configuration
ROOT_URLCONF = 'mymarketplace.urls'

# Template settings with context processors for Django and Allauth
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI application
WSGI_APPLICATION = 'mymarketplace.wsgi.application'

# Database settings (using MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartisp',  # Replace with your database name
        'USER': '   ',  # Replace with your database user
        'PASSWORD': '   ',  # Replace with your database password
        'HOST': 'localhost',  # Database host, usually 'localhost'
        'PORT': '3306',  # MySQL default port
        'OPTIONS': {
            'unix_socket': '/var/run/mysqld/mysqld.sock',  # Ensure correct socket path
        },
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

# Email backend settings


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'VOTRE_GOOGLE_CLIENT_ID',
            'secret': 'VOTRE_GOOGLE_CLIENT_SECRET',
            'key': ''
        }
    },
    'facebook': {
        'APP': {
            'client_id': 'VOTRE_FACEBOOK_CLIENT_ID',
            'secret': 'VOTRE_FACEBOOK_CLIENT_SECRET',
            'key': ''
        }
    },
    'twitter': {
        'APP': {
            'client_id': 'VOTRE_TWITTER_CLIENT_ID',
            'secret': 'VOTRE_TWITTER_CLIENT_SECRET',
            'key': ''
        }
    },
    # Ajoutez d'autres fournisseurs ici
}
