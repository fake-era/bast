from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.exceptions import PasswordNotEqualError, UserNotActiveError
from apps.common.swagger_params import token_params
from apps.common.views import CustomPermissionApiView

from apps.user.models import User
from apps.user.selectors import get_email_from_token, get_user
from apps.user.serializers import (AuthenticationInputSerializer,
                                   AuthenticationOutputSerializer,
                                   DetailOutputSerializer,
                                   RegistrationInputSerializer,
                                   RegistrationOutputSerializer,
                                   ResetForgotPasswordInputSerializer,
                                   UserChangePasswordInputSerializer,
                                   UserForgotPasswordInputSerializer,
                                   UserProfileOutputSerializer)
from apps.user.services import (change_user_forgot_password,
                                change_user_old_password_to_new,
                                create_user_by_email,
                                send_forgot_password_token,
                                send_verification_token)


class RegistrationApi(CustomPermissionApiView):
    api_description = 'User Registration'
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @swagger_auto_schema(
        operation_summary='Registration',
        operation_description=api_description,
        operation_id='Registration',
        request_body=RegistrationInputSerializer,
        responses={status.HTTP_201_CREATED: RegistrationOutputSerializer},
    )
    def post(self, request):
        serializer = RegistrationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        if data['password'] != data['repeat_password']:
            raise PasswordNotEqualError

        del data['repeat_password']

        send_verification_token(email=data['email'])
        created_user = create_user_by_email(**data)

        return Response(
            status=status.HTTP_201_CREATED,
            data=RegistrationOutputSerializer(created_user.token).data,
        )


class VerifyEmailApi(APIView):
    api_description = 'E-mail Verification'
    authentication_classes = ()
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary="VerifyEmail",
        operation_description=api_description,
        operation_id="VerifyEmail",
        manual_parameters=[
            token_params,
        ],
        responses={status.HTTP_200_OK: DetailOutputSerializer()}
    )
    def get(self, request):
        token = request.GET.get('token')

        email = get_email_from_token(token)

        user: User = get_user(email=email)
        user.is_active = True
        user.save()

        return Response(status=status.HTTP_200_OK)


class AuthenticationApi(CustomPermissionApiView):
    api_description = 'User Authentication'
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @swagger_auto_schema(
        operation_summary='Authentication',
        operation_description=api_description,
        operation_id='Authentication',
        request_body=AuthenticationInputSerializer,
        responses={status.HTTP_200_OK: AuthenticationOutputSerializer},
    )
    def post(self, request):
        serializer = AuthenticationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        user = authenticate(
            request,
            username=data['email'],
            password=data['password'],
        )

        if user is None:
            raise AuthenticationFailed

        if not user.is_active:
            raise UserNotActiveError

        login(request, user)

        return Response(
            data=AuthenticationOutputSerializer(user.token).data,
            status=status.HTTP_200_OK,
        )
