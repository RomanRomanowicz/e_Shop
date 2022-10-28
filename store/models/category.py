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