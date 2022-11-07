from os.path import abspath, dirname, join
from typing import Tuple

from corsheaders.defaults import default_headers, default_methods
from decouple import config

BASE_DIR: str = dirname(dirname(dirname(abspath(__file__))))

ALLOWED_HOSTS: Tuple = ("*",)
API_URL: str = config("API_URL", cast=str)

CSRF_TRUSTED_ORIGINS: Tuple = (API_URL,)

# Django
DEBUG: bool = config("DEBUG", default=True, cast=bool)
SECRET_KEY: str = config("SECRET_KEY", cast=str)

ROOT_URLCONF: str = "config.urls"
WSGI_APPLICATION: str = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "ATOMIC_REQUESTS": config("ATOMIC_REQUESTS", cast=bool, default=False),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT", cast=int),
        "CONN_MAX_AGE": config("CONN_MAX_AGE", cast=int, default=0),
        "OPTIONS": {
            "connect_timeout": 10,
            "options": "-c statement_timeout=15000ms"
        },
    }
}

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

# File access
STATIC_URL: str = "/static/"
STATIC_ROOT: str = join(BASE_DIR, "staticfiles")
MEDIA_URL: str = "/media/"
MEDIA_ROOT: str = join("media")

# Django Admin
DJANGO_SUPERUSER_EMAIL: str = config("DJANGO_SUPERUSER_EMAIL", cast=str)

DJANGO_SUPERUSER_PASSWORD: str = config("DJANGO_SUPERUSER_PASSWORD", cast=str)

# Security
SECURE_BROWSER_XSS_FILTER: bool = True
X_FRAME_OPTIONS: str = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF: bool = True

CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE: bool = config(
    "CSRF_COOKIE_SECURE",
    default=False,
    cast=bool
)
SESSION_COOKIE_SECURE: bool = config(
    "SESSION_COOKIE_SECURE",
    default=False,
    cast=bool
)

# # # Localization
LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('ru', 'Russian'),
    ('en', 'English'),
]
USE_I18N = True

USE_L10N: bool = True
TIME_ZONE: str = config("TIME_ZONE", default="Asia/Almaty", cast=str)
USE_TZ: bool = True

# CorsHeaders
CORS_ORIGIN_ALLOW_ALL: bool = True
CORS_ALLOW_METHODS: Tuple = default_methods
CORS_ALLOW_HEADERS: Tuple = default_headers
CORS_ALLOW_CREDENTIALS: bool = True

if DEBUG:
    from typing import Callable, Dict, Tuple

    from django.http import HttpRequest

    def show_toolbar(request: HttpRequest) -> bool:
        return True

    DEBUG_TOOLBAR_CONFIG: Dict[str, Callable] = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar
    }
    PANELS: str = "debug_toolbar.panels."
    DEBUG_TOOLBAR_PANELS: Tuple[str, ...] = (
        f"{PANELS}versions.VersionsPanel",
        f"{PANELS}timer.TimerPanel",
        f"{PANELS}settings.SettingsPanel",
        f"{PANELS}headers.HeadersPanel",
        f"{PANELS}request.RequestPanel",
        f"{PANELS}redirects.RedirectsPanel",
        f"{PANELS}staticfiles.StaticFilesPanel",
        f"{PANELS}sql.SQLPanel",
        f"{PANELS}templates.TemplatesPanel",
        f"{PANELS}cache.CachePanel",
        f"{PANELS}signals.SignalsPanel",
        f"{PANELS}logging.LoggingPanel",
    )
