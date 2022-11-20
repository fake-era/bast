from rest_framework import status
from rest_framework.exceptions import APIException


class ApiKeyNotVerifiedError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Api Key token not verified"
    default_code = 'ApiKeyNotVerified'


class UserNotActiveError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "User is not active"
    default_code = 'UserNotActive'


class UserNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User not found"
    default_code = 'UserNotFound'


class PasswordNotValidError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Password is not valid"
    default_code = 'PasswordNotValid'


class PasswordNotEqualError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Passwords not equal"
    default_code = 'PasswordNotEqual'


class PasswordsEqualError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Passwords are equal"
    default_code = 'PasswordsEqual'
