"""This file contains utility functions"""
from io import BytesIO
from PIL import Image
from django.conf import settings
from django.core.files import File
from django.db.models.fields.files import ImageFieldFile
from core.models import User
# --------------------------------------------------------------------------


def get_user_ava_path(
        instance: 'participant.Client', filename: str) -> str:
    """This function returns the path for the current user avatar image
    :param instance: an instance of the Client model
    :param filename: a string representing the name of the image file
    :return: a string representing the path for the user avatar image
    """
    return f'{settings.AVA_ROOT}/{instance.email}/{filename}'


def create_user(data: dict) -> User:
    """This function creates a user by using the provided data
    :param data: a dictionary representing the user data
    :return: a User instance
    """
    user = User.objects.create_user(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
    )
    return user


def get_ava_with_watermark(avatar: ImageFieldFile) -> File:
    """This function serves to change user avatar by watermarking
    :param avatar: a ImageFieldFile instance
    :return: a File instance
    """
    watermark = Image.open(settings.WATERMARK_IMAGE)
    ava = Image.open(avatar)
    ava_io = BytesIO()
    ava.paste(
        watermark, (ava.width - watermark.width, ava.height - watermark.height),
        mask=watermark)

    ava.save(ava_io, 'JPEG')

    return File(ava_io, avatar.name)
