from django.db import models
from utils import get_user_ava_path
# ---------------------------------------------------------------------------


class Client(models.Model):

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

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Client({self.email}, {self.first_name}, {self.gender})'

