from email.policy import default
from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

from core.settings import DOMAIN

# button_link_example = '<a href="" class="btn btn-primary">Подробнее</a>' % DOMAIN

class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=True, null=True)
    description = RichTextField( verbose_name='Описание', blank=True, null=True)
    image = ImageField(upload_to='slides/', verbose_name='Изображение')
    button_link = models.URLField(max_length=200, blank=True, null=True, verbose_name='Ссылка для кнопки', default='Например: %s/form' % DOMAIN,)
    button_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Текст кнопки')
    order = models.IntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['order', '-updated_at']