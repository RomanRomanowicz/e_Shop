from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='наименование категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='SLUG')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])


class CategoryGender(models.Model):
    gender = models.CharField(max_length=200, db_index=True, blank=True, null=True, verbose_name='Категория по полу')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='SLUG')

    class Meta:
        ordering = ('gender',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория по полу'

    def __str__(self):
        return self.gender

    def get_absolute_url(self):
        return reverse('store:gender_list', args=[self.slug])


class CategoryColor(models.Model):
    color = models.CharField(max_length=200, db_index=True, verbose_name='Категория по цвету')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='SLUG')

    class Meta:
        ordering = ('color',)
        verbose_name = 'Категория по цвету'
        verbose_name_plural = 'Категория по цвету'

    def __str__(self):
        return self.color

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])


class CategorySize(models.Model):
    size = models.CharField(max_length=200, db_index=True, verbose_name='Категория по размеру')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='SLUG')

    class Meta:
        ordering = ('size',)
        verbose_name = 'Категория по размеру'
        verbose_name_plural = 'Категория по размеру'

    def __str__(self):
        return self.size

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])