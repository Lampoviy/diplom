from django.db import models

class Yslugi(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    urlyoutube = models.CharField(max_length=500, unique=True, blank=True, null=True,verbose_name='Ссылка на видео')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')


    class Meta:
        db_table = 'product'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ("id",)
        
    def __str__(self):
        return f'{self.name}'
