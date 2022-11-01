from django.contrib import admin
from store.models.category import Category, CategoryGender
from store.models.order import Order, OrderItem
from store.models.products import Products


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProductsAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(CategoryGender)


@admin.register(CategoryGender)
class CategoryGender(admin.ModelAdmin):
    list_display =('gender', 'name', 'slug')
    prepopulated_fields = {"slug": ("gender", )}