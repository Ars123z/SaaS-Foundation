"""
Django settings for cfehome project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from decouple import config
from pathlib import Path
from os import getenv
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('DJANGO_SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = str(os.environ.get("DJANGO_DEBUG")).lower() == "true"
DEBUG = getenv('DJANGO_DEBUG')

print("DEBUG", DEBUG, type(DEBUG))

ALLOWED_HOSTS = [
    ".railway.app" # https://saas.prod.railway.app
]
if DEBUG:
    ALLOWED_HOSTS += [
        "127.0.0.1",
        "localhost"
    ]


# Application definition

INSTALLED_APPS = [
    # django-apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # my-apps
    "visits",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cfehome.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cfehome.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Add these at the top of your settings.py

# .env content for your reference

# DJANGO_SECRET_KEY="django-insecure-3x@#1$2%3^4&5*6(7)8_9+0!a-b=c~d[e]f{g}h|i\j:k;l<m>n?o/p
# "
# DJANGO_DEBUG="True"
# DATABASE_URL="postgresql://neondb_owner:RI0j9bQwqzpN@ep-frosty-sun-a6di196y.us-west-2.aws.neon.tech/neondb?sslmode=require"
# PGHOST='ep-frosty-sun-a6di196y.us-west-2.aws.neon.tech'
# PGDATABASE='neondb'
# PGUSER='neondb_owner'
# PGPASSWORD='RI0j9bQwqzpN'


# Add these at the top of your settings.py


# Initialize environment variables


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('PGDATABASE'),
        'USER': getenv('PGUSER'),
        'PASSWORD': getenv('PGPASSWORD'),
        'HOST': getenv('PGHOST'),
        'PORT': getenv('PGPORT', default=5432),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}



# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'neondb',
#     'USER': 'neondb_owner',
#     'PASSWORD': 'RI0j9bQwqzpN',
#     'HOST': 'ep-frosty-sun-a6di196y.us-west-2.aws.neon.tech',
#     'PORT': 5432,
#     'OPTIONS': {
#       'sslmode': 'require',
#     },
#   }
# }





# Add these at the top of your settings.py
# from os import getenv
# from dotenv import load_dotenv

# Replace the DATABASES section of your settings.py with this
# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': config('PGDATABASE'),
#     'USER': config('PGUSER'),
#     'PASSWORD': config('PGPASSWORD'),
#     'HOST': config('PGHOST'),
#     'PORT': config('PGPORT', 5432),
#     'OPTIONS': {
#       'sslmode': 'require',
#     },
#   }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"