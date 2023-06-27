"""This file contains serializers for Client model"""
from rest_framework import serializers
from participant.models import Client
from core.models import User
# -------------------------------------------------------------------------


class ClientRegisterSerializer(serializers.ModelSerializer):
    """This class is serializer to register a new client"""
    username = serializers.CharField(required=False, max_length=30)
    password = serializers.CharField(min_length=7, max_length=30)
    password_repeat = serializers.CharField(min_length=7, max_length=30)

    class Meta:
        model = Client
        exclude = ['user']

    def validate(self, attrs: dict) -> dict:
        password = attrs.get('password')
        password_repeat = attrs.get('password_repeat')
        username = attrs.get('username')
        email = attrs.get('email')

        if email and not username:
            try:
                attrs['username'] = email.split('@')[0]
            except Exception:
                attrs['username'] = email

        if password != password_repeat:

            raise serializers.ValidationError(
                {'password, password_repeat': 'The passwords do not match'})

        attrs.pop('password_repeat', None)
        self.fields.pop('password', None)
        self.fields.pop('password_repeat', None)

        return super().validate(attrs)

    def create(self, validated_data: dict) -> Client:
        user_data = validated_data.copy()

        user_data.pop('password_repeat', None)
        user_data.pop('gender', None)

        try:
            user = User.objects.create_user(**user_data)
        except Exception as e:
            raise serializers.ValidationError({
                'error': f'cannot create user, the error: {e}'
            })

        validated_data['user_id'] = user.pk
        validated_data.pop('username', None)
        validated_data.pop('password', None)

        return super().create(validated_data)
