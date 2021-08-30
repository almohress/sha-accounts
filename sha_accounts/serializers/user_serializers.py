from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from ..models.user_models import User
from .profile_serializers import ProfileSerializer


class UserSignUpRequest(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super().create(validated_data)


class UserSignUpResponse(WritableNestedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'profile']
