

from pathlib import Path
from datetime import timedelta
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CLOUDINARY_URL='cloudinary://771963873543859:_kYKWnZ6-6LE8gSfiYGaA0XnBAY@dsluf9vsu'
cloudinary.config(
    cloud_name = 'dsluf9vsu',
    api_key =  '771963873543859',
    api_secret = '_kYKWnZ6-6LE8gSfiYGaA0XnBAY',

)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=4#6f=i6xaf0&l55yhg@)86figc@&gh3x*)p=p=7tf%@zx=vy5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["10.0.2.2", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'post',
    'rest_framework',
    'djoser',
    'corsheaders',
    'social_django',
    'rest_framework_simplejwt',

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS =  True

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
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect'
            ],
        },
    },
]

ANYMAIL= { 
"SENDINBLUE_API_KEY" : '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',
} 
DEFAULT_FROM_EMAIL="expensive7832@gmail.com"
EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_USER_MODEL = "account.User"
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thread',
        'USER': 'root',
        'PASSWORD': 'rrrrrrrrrrr'
    }
}



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

SIMPLE_JWT = {
   'ACCESS_TOKEN_LIFETIME': timedelta(days=60),
   'REFRESH_TOKEN_LIFETIME': timedelta(days=60),
   "AUTH_HEADER_TYPES": ("Bearer","JWT"),

}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    
    ),
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [ 'http://127.0.0.1:3000', 'http://127.0.0.1:8081'],
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    # 'ACTIVATION_URL': 'auth/users/activation/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SERIALIZERS': {
        
    },
}

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

AUTHENTICATION_BACKENDS = [
    "djoser.social.backends.facebook.FacebookOAuth2Override",
    "social_core.backends.google.GoogleOAuth2",
    'social_core.backends.twitter.TwitterOAuth',
    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['state']
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = None
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name','gender', 'password']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '349620980999-89eibic3egumkar2pnv5hqv8n33lt2mg.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'dl9ypfcyb',
#     'API_KEY': '994519587245655',
#     'API_SECRET': 'DxZMe3Cn0ZGR5ujKnKscMe60q0g',
# }

CORS_ALLOW_ALL_ORIGINS = True
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
