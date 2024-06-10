from django.db import models
from users.models import User
from yslugi.models import Yslugi

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    ysluga = models.ForeignKey(to=Yslugi, on_delete=models.CASCADE, verbose_name='Услуга')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Курсы пользователя"
        verbose_name_plural = "Курсы пользователей"
        
    def __str__(self) ->str:
        return f'{self.user.username} приобрел курс "{self.ysluga.name}"'  