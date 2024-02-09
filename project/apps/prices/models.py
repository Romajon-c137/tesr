from django import db
from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField


class Analysis(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    imege = ImageField(upload_to='analysis/', verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        db_table = 'analysis'
