import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '+1dx75zg6url%quwf_t$mtnepbl2+wthv*n$b2-=35$gse3k)a'

DEBUG = True

ALLOWED_HOSTS = ['.ngrok.io', '127.0.0.1', '.herokuapp.com', 'localhost', '0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'evaluation',
    'kenindus.utils',
    'oauth2_provider',
    'corsheaders',
    'jsonfield',

    'rest_framework',
    'easy_pdf',
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kenindus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
	    ,
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

WSGI_APPLICATION = 'kenindus.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'live/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'live/media')
# AfricasTalkingGatways
ATG_USERNAME = "my_trial_app"
ATG_API_KEY = "5a090d4a7da6b2e8567996684289a0dc2105a9dcda3d27c82478a59b86d7d6b4"
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# __DEFAULT_KENINDUS_ADMIN_NAME = "Kenindus Admin"
# __DEFAULT_KENINDUS_ADMIN_EMAIL = "admin@asks.me"
# __DEFAULT_FROM_EMAIL = 'noreply@kenindus.com'
# ADMIN_NAME = __DEFAULT_KENINDUS_ADMIN_NAME
# ADMIN_EMAIL = __DEFAULT_KENINDUS_ADMIN_EMAIL
# ADMIN_LOCATION = "Eldoret, KENYA"
# ADMINS = (
#     (ADMIN_NAME, ADMIN_EMAIL),
# )
# SERVER_EMAIL = DEFAULT_FROM_EMAIL = __DEFAULT_FROM_EMAIL
# EMAIL_REPLY_PATTERN = "reply+%s+code@keninduss.io"
# EMAIL_FROM_PATTERN = u'''"%s on Kenindus" <%s>'''
# EMAIL_REPLY_SECRET_KEY = "abc"
# EMAIL_REPLY_SUBJECT = u"[kenindus] %s"
# EMAIL_REPLY_REMOVE_QUOTED_TEXT = True
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'deisaack@gmail.com'
EMAIL_HOST_PASSWORD = 'Jacktone1'
# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# KENINDUS_ADMIN_EMAIL = "admin@me.com"
EMAIL_USE_TLS = True

SESSION_SAVE_EVERY_REQUEST = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_HTTPONLY = True


AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    'django.contrib.auth.backends.ModelBackend'
    # '...',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

CORS_ORIGIN_WHITELIST = (
    'sandbox.safaricom.co.ke',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


MPESA_IPN_USER = 'username'
MPESA_IPN_PASS = 'password'
MPESA_PAYBILL_NUMBER = '123456'
