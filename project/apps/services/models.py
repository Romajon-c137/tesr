from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    is_active=models.BooleanField(default=True, verbose_name='Активна')
    description = RichTextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "s_category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Service(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'service'
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    title = models.CharField(max_length=200, verbose_name="Названия")
    image = ImageField(upload_to='images', blank=True, verbose_name="Изображение")
    description = RichTextField(verbose_name="Описание")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.SlugField(verbose_name="Ярлык", unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Рубрика', related_name='service_category')
    seo_title = models.CharField(max_length=200, verbose_name="SEO Title", blank=True)
    seo_description = models.CharField(max_length=300, verbose_name="SEO Description", blank=True)

    def get_absolute_url(self):
        return '%s-%s' % (self.slug, self.pk)
