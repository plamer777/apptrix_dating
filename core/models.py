from django.contrib.auth.models import AbstractUser
# ------------------------------------------------------------------------


class User(AbstractUser):
    """This class represents a custom user model"""
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'User({self.username}, {self.email})'
