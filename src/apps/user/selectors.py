from typing import Optional

from django.core.cache import cache

from apps.common.exceptions import UserNotFoundError
from apps.user.models import User


def get_email_from_token(token: str) -> str:
    fetched_email = cache.get(token)
    cache.delete(token)
    return fetched_email


def get_user(
        **kwargs
) -> User:
    fetched_user: Optional[User] = User.objects.filter(
        **kwargs
    ).first()
    if fetched_user is None:
        raise UserNotFoundError
    return fetched_user
