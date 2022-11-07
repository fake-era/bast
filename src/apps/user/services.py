import uuid

from django.conf import settings
from django.core.cache import cache
from django.template.loader import render_to_string

from apps.common.exceptions import (PasswordNotEqualError,
                                    PasswordNotValidError, PasswordsEqualError)
from apps.common.utils.email import EmailSender
from apps.user.models import User


def create_user_by_email(
        email: str,
        password: str,
        **extra_fields
) -> User:
    return User.objects.create_user(
        email=email,
        password=password,
        **extra_fields
    )


def send_verification_token(*, email: str) -> None:
    print("sending")

    generated_token = str(uuid.uuid4())

    cache.set(generated_token, email, timeout=settings.CACHE_TTL)
    absurl = f"{settings.API_URL}/v1/auth/email-verify?token={generated_token}"
    context = {"email": email, "verification_link": absurl}
    email_body = render_to_string("media/mail/verf.html", context)

    email_sender = EmailSender()
    email_sender.send(
        subject='Verify your email',
        message=email_body,
        email=email
    )


def send_forgot_password_token(*, email: str) -> None:
    generated_token = str(uuid.uuid4())

    cache.set(generated_token, email, timeout=settings.CACHE_TTL)
    absurl = f"{settings.API_URL}/set-new-password?token={generated_token}"
    context = {"reset_link": absurl}
    email_body = render_to_string("media/reset/index.html", context)

    email_sender = EmailSender()
    email_sender.send(
        subject='Password reset',
        message=email_body,
        email=email
    )


def change_user_old_password_to_new(
        *,
        user: User,
        old_password: str,
        new_password: str
) -> User:
    if old_password == new_password:
        raise PasswordsEqualError
    if not user.check_password(old_password):
        raise PasswordNotValidError
    user.set_password(new_password)
    user.save()
    return user


def change_user_forgot_password(
        *,
        user: User,
        password_1: str,
        password_2: str
) -> User:
    if password_1 != password_2:
        raise PasswordNotEqualError
    user.set_password(password_1)
    user.save()
    return user
