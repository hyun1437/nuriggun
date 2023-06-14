"""
Django settings for nuriggun project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv
import my_settings
from corsheaders.defaults import default_methods


DATABASES = my_settings.DATABASES

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(PROJECT_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'user',
    'article',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
]

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nuriggun.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'nuriggun.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1:5500',
    'http://localhost:5500',
]

CSRF_TRUSTED_ORIGINS  =  [ 
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1:5500',
    'http://localhost:5500',
]

CORS_ALLOW_METHODS = list(default_methods) + [
    "",
]


CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000',
                         'http://localhost:5000',
                         'http://localhost:5500',
                         'http://127.0.0.1:5500',
                         'http://localhost:8000',
                         'http://127.0.0.1:8000',
                        ]


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5000),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.environ.get('SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",

}

AUTHENTICATION_BACKENDS = [ # 소셜로그인 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# 사이트 1개만 사용
SITE_ID = 1

REST_USE_JWT = True

# dj-rest-auth 3.0 버전 이후로는 이렇게 써야함
# JWT_AUTH_HTTPONLY : 쿠키를 http only 여부
# JWT_AUTH_REFRESH_COOKIE : refresh token을 담을 쿠키 이름
# JWT_AUTH_COOKIE_USE_CSRF : JWT 쿠키 csrf 검사
# SESSION_LOGIN : 세션 로그인
REST_AUTH = {
    'USE_JWT' : True,
    'JWT_AUTH_HTTPONLY': False,
    'JWT_AUTH_REFRESH_COOKIE' : "refresh_token",
    "JWT_AUTH_COOKIE": "access",
    'JWT_AUTH_COOKIE_USE_CSRF' : True,
    'SESSION_LOGIN' : False
}


AUTH_USER_MODEL = 'user.User'
# 소셜로그인부분 ! 
ACCOUNT_UNIQUE_EMAIL = True # 이메일을 유니크로 쓸것인지
ACCOUNT_USER_MODEL_USERNAME_FIELD = None #유저 네임 필드가 없어도 됨
ACCOUNT_USERNAME_REQUIRED = False # 아이디로 로그인 하지않고 
ACCOUNT_EMAIL_REQUIRED = True # 이메일로 로그인하게 만듦
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = '/' # 로그인되면 리다이렉트 될 페이지 프론트로 해야겠죠 ? 만들면 주석풀기 ~
ACCOUNT_LOGOUT_REDIRECT_URL = '/' #이건 로그아웃 로그아웃 요청은 /accounts/logout 여기임! 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # 메일 호스트 서버
EMAIL_PORT = '587' # naver와 통신하는 포트
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER") # 발신할 이메일
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") # 발신할 메일의 비밀번호
EMAIL_USE_TLS = True # TLS 보안 방법
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
URL_FRONT = 'http://127.0.0.1:5500/user/index.html' # 공개적인 웹페이지가 있다면 등록
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True # 유저가 받은 링크를 클릭하면 회원가입 완료되게끔
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_EMAIL_SUBJECT_PREFIX = "[nuriggun]" # 이메일에 자동으로 표시되는 사이트 정보
# PASSWORD_RESET_TIMEOUT = 86400 # 비밀번호 재설정 만료 기간 (1일)


#소셜 로그인 관련
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',    
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = 'http://127.0.0.1:5500/user/login.html'   # social login redirect
ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # logout redirect