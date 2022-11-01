from django.db import models
from .category import Category, CategoryGender
from django.urls import reverse


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='категория')
    gender = models.ForeignKey(CategoryGender, on_delete=models.CASCADE, related_name='products', verbose_name='Категория по полу')
    name = models.CharField(max_length=200, db_index=True, verbose_name='наименование товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='SLUG')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='фото')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    available = models.BooleanField(default=True, verbose_name='доступный')
    created = models.DateTimeField(auto_now_add=True, verbose_name=' дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:shop_list', args=[self.id, self.slug])

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()