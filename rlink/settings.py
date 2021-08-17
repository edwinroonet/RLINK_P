"""
Django settings for rlink project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os, datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_PATH = os.getcwd()+""


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*hn6j#!gyos$!207fw82cm355lwpdpjle11i3sov065qqp2!@)'
ALGORITHM = 'HS256'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


CERTIFIED_MAIL = "homenmove9@gmail.com"
CERTIFIED_PW = "tongin9!"
FIREBASE_API_KEY = "AIzaSyAbJDChxmn4Fl_tPMzswuZThMFNuh4nR4M"

# Application definition

INSTALLED_APPS = [
    'web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rlink.urls'

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
            'libraries':{
               'split': 'web.templatetags.split',
            }
        },
    },
]

WSGI_APPLICATION = 'rlink.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'segong',
        'USER': 'segong',
        'PASSWORD': 'segong1!',
        'HOST': '118.67.135.90',
        #'NAME': 'RLINK_DEV',
        #'USER': 'rlinkdev',
        #'PASSWORD': 'rdev210730!',
        #'HOST': '61.74.156.122',
        #'PORT': '3366',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]


#
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 포맷터 (텍스트의 포맷 형식 정의, 여러 포맷 정의 가능)
    'formatters': {
        'fileFormat': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        }
    },
    # 핸들러 (로그 레코드로 무슨 작업을 할 것인지 정의, 여러 핸들러 정의 가능)
    'handlers': {
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/logfile.log'),
            'encoding': 'UTF-8',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'fileFormat',
        },
        # 콘솔(터미널)에 출력
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'fileFormat',
        }
    },
    'loggers': {
        # 로거 종류
        'web': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'mobile': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'partner': {
            'handlers': ['file'],
            'level': 'DEBUG',
        }
    },
}
