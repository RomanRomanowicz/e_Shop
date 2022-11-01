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
    CATEGORY_GENDER = (
        ('M', "Men's dresses"),
        ('W', "Women's dresses"),
        ('B', "Baby's dresses"),
    )
    gender = models.CharField(max_length=1, choices=CATEGORY_GENDER, blank=True, default='d', help_text='Категория по полу')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='SLUG')
    name = models.CharField(max_length=200, db_index=True, blank=True, null=True, verbose_name='Категория по полу')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория по полу'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:gender_list', args=[self.slug])