from typing import Tuple

from decouple import config

DEBUG: bool = config("DEBUG", default=True, cast=bool)

DJANGO_APPS: Tuple[str, ...] = (
    'django.contrib.sites',
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sessions",
)
SIDE_APPS: Tuple[str, ...] = (
    "corsheaders",
    "rest_framework",
    "django_extensions",
    "django_filters",
    "drf_yasg",
    "rest_framework_simplejwt",
)
DEBUG_APPS: Tuple[str, ...] = ("debug_toolbar",)

PROJECT_APPS: Tuple[str, ...] = (
    "apps.book.apps.BookAppConfig",
    "apps.user.apps.UserAppConfig",
)

INSTALLED_APPS: Tuple[str, ...] = DJANGO_APPS + SIDE_APPS + PROJECT_APPS

if DEBUG:
    INSTALLED_APPS += DEBUG_APPS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
