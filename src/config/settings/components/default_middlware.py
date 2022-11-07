from typing import Tuple

from decouple import config

DEBUG: bool = config("DEBUG", default=True, cast=bool)

DJANGO_MIDDLEWARE: Tuple = (
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

)
SIDE_MIDDLEWARE: Tuple = (
    "corsheaders.middleware.CorsMiddleware",
)
DEBUG_MIDDLEWARE: Tuple[str, ...] = (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # 'silk.middleware.SilkyMiddleware',
)

BEFORE: Tuple = DJANGO_MIDDLEWARE[:3]
AFTER: Tuple = DJANGO_MIDDLEWARE[3:]
MIDDLEWARE: Tuple = BEFORE + SIDE_MIDDLEWARE + AFTER

if DEBUG:
    MIDDLEWARE += DEBUG_MIDDLEWARE
