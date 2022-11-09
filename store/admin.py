from django.contrib import admin
from store.models.category import Category, CategoryGender, CategoryColor, CategorySize
from store.models.order import Order, OrderItem
from store.models.products import Products, Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ImageInline(admin.TabularInline):
    model = Image


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('image', )
    # inlines = [ImageInline]


admin.site.register(Products, ProductsAdmin)

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display =('name', 'image')

admin.site.register(Image)




# admin.site.register(Image, ImageAdmin)
# admin.site.register(Products, ProductsAdmin)

admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(CategoryGender)


@admin.register(CategoryGender)
class CategoryGenderAdmin(admin.ModelAdmin):
    list_display =('gender', 'slug')
    prepopulated_fields = {"slug": ("gender", )}


@admin.register(CategoryColor)
class CategoryColorAdmin(admin.ModelAdmin):
    list_display =('color', 'slug')
    prepopulated_fields = {"slug": ("color", )}

@admin.register(CategorySize)
class CategorySizeAdmin(admin.ModelAdmin):
    list_display =('size', 'slug')
    prepopulated_fields = {"slug": ("size", )}


# class PhotoInline(admin.StackedInline):
#     model = Image
#     extra = 1
#
#
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['image', ]
#     inlines = [PhotoInline]

    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #
    #     for afile in request.FILES.getlist('image'):
    #         obj.photos.create(image=afile)


# admin.site.register(Image, ImageAdmin)