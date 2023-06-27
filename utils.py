"""This file contains utility functions"""
from string import ascii_lowercase, digits
from random import sample
from io import BytesIO
from PIL import Image
from django.conf import settings
from django.core.files import File
from django.core.mail import send_mail
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
    ava_name = ''.join(sample(ascii_lowercase+digits, 15))
    ava_extension = filename.split('.')[-1]
    return f'{settings.AVA_ROOT}/{instance.email}/{ava_name}.{ava_extension}'


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
    watermark.close()
    ava.close()

    return File(ava_io, avatar.name)


def send_message(
        client_from: 'participant.Client', client_to: 'participant.Client',
        email_from: str = settings.EMAIL_HOST_USER,
        subject: str = settings.MESSAGE_SUBJECT,
        template: str = settings.MESSAGE_TEMPLATE,
) -> int:
    """This function sends a message to the user email addresses by provided
    template
    :param client_from: a Client instance to send the message from
    :param client_to: a Client instance to send the message to
    :param email_from: the email address of SMTP host
    :param subject: the subject of the email message
    :param template: the template of the email message
    """
    message = template.format(
        client_from.first_name, client_from.email)
    return send_mail(
        subject, message, email_from, recipient_list=[client_to.email])

