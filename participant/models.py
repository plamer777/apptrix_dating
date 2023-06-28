"""The file contains a Client model representing client table of the database"""
from django.db import models
from utils import get_user_ava_path, get_ava_with_watermark
# ---------------------------------------------------------------------------


class Client(models.Model):
    """The Client model contains all necessary fields"""
    class Gender(models.IntegerChoices):
        man = (1, 'Мужчина')
        woman = (2, 'Женщина')
        not_answer = (3, 'Нет ответа')

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, null=False)
    ava = models.ImageField(upload_to=get_user_ava_path, blank=True, null=True)
    email = models.EmailField()
    gender = models.SmallIntegerField(choices=Gender.choices)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    favorites = models.ManyToManyField('self', symmetrical=False)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        return f'Клиент({self.email}, {self.first_name}, {self.gender})'
