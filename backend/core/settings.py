from pathlib import Path
from datetime import timedelta

from decouple import config # Load environment variables from.env file


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',

    'users',
    'api',
    
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('POSTGRES_DB_NAME'),
    'USER': config('POSTGRES_DB_USER'),
    'PASSWORD': config('POSTGRES_DB_PASSWORD'),
    'HOST': 'localhost',
    'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Rest framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.authentication.CookieJWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # Short-lived access token
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Long-lived refresh token
    'ROTATE_REFRESH_TOKENS': True,                   # New refresh token on refresh
    'BLACKLIST_AFTER_ROTATION': True,                # Invalidate old refresh tokens
    
    'AUTH_COOKIE': 'access_token',      # Cookie name for access token
    'AUTH_COOKIE_DOMAIN': None,         # Domain for cookie (None for localhost)
    'AUTH_COOKIE_SECURE': True,         # Send cookie only over HTTPS
    'AUTH_COOKIE_HTTP_ONLY': True,      # Prevent JavaScript access
    'AUTH_COOKIE_SAMESITE': 'Lax',      # SameSite policy
    
    'UPDATE_LAST_LOGIN': True,                    # Update last login timestamp when refreshing token
    'ALGORITHM': 'HS256',                            # Encryption algorithm
    'SIGNING_KEY': config('SECRET_KEY'),                       # Django secret key
    
    
    'USER_ID_FIELD': 'email',   # Use email as the identifier in JWT payload
    'USER_ID_CLAIM': 'user_id',  # Claim name in JWT payload
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


AUTH_USER_MODEL = 'users.CustomUser'