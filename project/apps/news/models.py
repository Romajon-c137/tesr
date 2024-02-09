from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = RichTextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "n_category"
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"


class News(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    title = models.CharField(max_length=200, verbose_name="Названия")
    image = ImageField(upload_to='images', blank=True, verbose_name="Изображение")
    description = RichTextField(verbose_name="Описание")
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.SlugField(verbose_name="Ярлык", unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Рубрика', related_name='news_category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='news_author')
    seo_title = models.CharField(max_length=200, verbose_name="SEO Title", blank=True)
    seo_description = models.CharField(max_length=300, verbose_name="SEO Description", blank=True)

    def get_absolute_url(self):
        return '%s-%s' % (self.slug, self.pk)

    def get_image_url(self):
        if self.image:
            return '/media/%s' % (self.image)
        else:
            return '/static/images/150x150.png'