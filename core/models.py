"""The file contains a User model representing user table of the database"""
from django.contrib.auth.models import AbstractUser
from django.db import models
# ------------------------------------------------------------------------


class User(AbstractUser):
    """This class represents a custom user model"""
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=150, unique=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'User({self.username}, {self.email})'
