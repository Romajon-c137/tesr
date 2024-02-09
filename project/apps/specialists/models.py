from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

ROLES = (
    (0, 'Руководство'),
    (1, 'Доктор'),
    (2, 'Врач'),
    (3, 'Медсестра'),
    (4, 'Лаборант'),
)

class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = RichTextField(blank=True, null=True)
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.SlugField(unique=True, verbose_name="Ярлык")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = RichTextField(verbose_name="Описание", null=True, blank=True)
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "departments"
        verbose_name = "Отделение"
        verbose_name_plural = "Отделение"


class Person(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    name = models.CharField(max_length=200, verbose_name="ФИО")
    image = ImageField(upload_to='images', verbose_name="Изображение")
    description = RichTextField(verbose_name="Биография", null=True, blank=True)
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.SlugField(verbose_name="Ярлык", unique=True)
    experience = models.IntegerField(verbose_name="Опыт работы", null=True, blank=True)
    roles = models.ManyToManyField(Role, verbose_name="Должносты", blank=True)
    role = models.IntegerField(choices=ROLES, verbose_name="Роль на сайте", default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отделение', related_name='person_department', null=True, blank=True)
    seo_title = models.CharField(max_length=200, verbose_name="SEO Title", blank=True)
    seo_description = models.CharField(max_length=300, verbose_name="SEO Description", blank=True)

    def get_absolute_url(self):
        return '%s-%s' % (self.slug, self.pk)
