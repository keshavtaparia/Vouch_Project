"""
Django settings for hardik project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')cheruc6&$12!@4dys=peqiqn(l4q-d8cmha0u!dr0jzs=usr_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.reddit', 
    'allauth.socialaccount.providers.twitter', 
    'django.contrib.auth', 
    'django.contrib.sites', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles',
    'reddit_posts',
] 

AUTHENTICATION_BACKENDS = ( 
    'django.contrib.auth.backends.ModelBackend', 
    'allauth.account.auth_backends.AuthenticationBackend', 
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [ 
  { 
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [ 
            os.path.normpath(os.path.join(BASE_DIR, 'Templates')), 
        ], 
        'APP_DIRS': True, 
        'OPTIONS': { 
            'context_processors': [ 
                'django.template.context_processors.debug', 
                'django.template.context_processors.request', 
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
                'django.template.context_processors.request', 
            ], 
        }, 
    }, 
]

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [ os.path.join(BASE_DIR, 'Templates'),],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

SOCIALACCOUNT_PROVIDERS = {
    'reddit': {
        'AUTH_PARAMS': {'duration': 'permanent'},
        'SCOPE': ['*'],
        'USER_AGENT': 'django:myappid:1.0 (by /u/yourredditname)',
    }
}

SITE_ID = 3
# # allout login settings
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/home/'
# AUTH_USER_MODEL = 'LocalUser.UserModel'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'