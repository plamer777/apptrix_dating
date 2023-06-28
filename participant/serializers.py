"""This file contains serializers for Client model"""
from django.db import transaction
from rest_framework import serializers
from participant.models import Client
from utils import create_user, get_ava_with_watermark
# -------------------------------------------------------------------------


class ClientRegisterSerializer(serializers.ModelSerializer):
    """This class is serializer to register a new client"""
    username = serializers.CharField(required=False, max_length=30)
    password = serializers.CharField(min_length=7, max_length=30)
    password_repeat = serializers.CharField(min_length=7, max_length=30)
    lat = serializers.FloatField(
        required=False, min_value=-90.0, max_value=90.0)
    lon = serializers.FloatField(
        required=False, min_value=-180.0, max_value=180.0)

    class Meta:
        model = Client
        exclude = ['user', 'favorites', 'distance']

    def validate(self, attrs: dict) -> dict:
        """This method validates user passwords during registration process
        and creates a username if it was not provided"""
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
        """This method serves to create a user model together with the client
        model
        :return: the created client model
        """
        try:
            with transaction.atomic():
                user = create_user(validated_data)
                validated_data['user_id'] = user.pk
                validated_data.pop('username', None)
                validated_data.pop('password', None)
                if validated_data.get('ava'):
                    validated_data['ava'] = get_ava_with_watermark(
                        validated_data.get('ava'))
                return super().create(validated_data)

        except Exception as e:
            raise serializers.ValidationError({
                'error': f'cannot create user, the error: {e}'
            })


class ClientUpdateSerializer(serializers.ModelSerializer):
    """This serializer serves to update a client favorites attribute"""
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = Client
        fields = ['email']


class ClientListSerializer(serializers.ModelSerializer):
    """This serializer serves to get a list of clients"""

    class Meta:
        model = Client
        exclude = ['distance']
