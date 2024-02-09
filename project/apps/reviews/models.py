from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Review(models.Model):
    """
    Model representing a review.
    """
    name = models.CharField(max_length=100, verbose_name='ФИО')
    review = RichTextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    class Meta:
        """
        Meta class to set some other options.
        """
        ordering = ('-created_at',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def get_absolute_url(self):
        return '/review/%s' % self.id