from rest_framework import serializers

from apps.user.models import User


class RegistrationInputSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField()

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'repeat_password',
        )


class RegistrationOutputSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)


class AuthenticationInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    token = serializers.CharField(max_length=255, read_only=True)


class AuthenticationOutputSerializer(serializers.Serializer):
    token = serializers.CharField()


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserForgotPasswordInputSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserChangePasswordInputSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()


class ResetForgotPasswordInputSerializer(serializers.Serializer):
    password_1 = serializers.CharField()
    password_2 = serializers.CharField()


class DetailOutputSerializer(serializers.Serializer):
    detail = serializers.CharField()
