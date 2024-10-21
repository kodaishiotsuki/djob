import os
from datetime import timedelta
from pathlib import Path

# BASE_DIR はプロジェクトの基本ディレクトリを指すパスです。これを使って他のファイルパスを簡単に取得できます。
BASE_DIR = Path(__file__).resolve().parent.parent

# 環境変数から機密情報を取得しています。SECRET_KEYはDjangoアプリケーションのセキュリティ上非常に重要なキーです。
SECRET_KEY = os.environ.get("SECRET_KEY")

# デバッグモードの設定。デバッグモードは開発時に有効にし、運用時には無効にする必要があります。
DEBUG = bool(os.environ.get("DEBUG", default=0))

# 許可するホスト名のリスト。環境変数からスペースで区切られたリストを取得しています。
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

USER_CREATE_PASSWORD_RETYPE = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',
    'job',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://localhost:3000',
    'http://localhost:8000',
]

CORS_ALLOW_CREDENTIALS = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djob_backend.urls'

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

WSGI_APPLICATION = 'djob_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),  
        'NAME': os.environ.get("SQL_DATABASE"), 
        'USER': os.environ.get("SQL_USER"),  
        'PASSWORD': os.environ.get("SQL_PASSWORD"), 
        'HOST': os.environ.get("SQL_HOST"),  
        'PORT': os.environ.get("SQL_PORT"),  
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


# 国際化の設定
LANGUAGE_CODE = 'en-us'  # 言語コード
TIME_ZONE = 'UTC'  # タイムゾーン
USE_I18N = True  # 国際化対応を有効化
USE_TZ = True  # タイムゾーンを有効化

# 静的ファイルの設定（CSSやJavaScriptなど）
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# プライマリキーのデフォルト設定
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
