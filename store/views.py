from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from store.forms import ImageForm
from store.models.products import Products, Category, CategoryGender, CategoryColor, CategorySize
from django.views.generic.base import View


""" home page """


class CatFil():
    """categories для вывода """
    def get_category(self):
        return Category.objects.all()

    def get_products(self):
        return Products.objects.filter(available=True)

    def get_category_gender(self):
        return CategoryGender.objects.all()

    def get_category_color(self):
        return CategoryColor.objects.all()

    def get_category_size(self):
        return CategorySize.objects.all()


# class HomePageView(View):
#     def get(self, request, category_slug=None):
#         category = None
#         categories = Category.objects.all()
#         products = Products.objects.filter(available=True)
#         if category_slug:
#             category = get_object_or_404(Category, slug=category_slug)
#             products = products.filter(category=category)
#         return render(request, 'store/index.html', {'category': category, 'categories': categories, 'products': products})


class HomePageView(CatFil, ListView):
    model = Products
    queryset = Products.objects.filter(available=True)
    context_object_name = 'product_list'
    template_name = 'store/base.html'

""" shop view """


# class ShopProductListView(View):
#     def get(self, request, category_slug=None):
#         category = None
#         categories = Category.objects.all()
#         products = Products.objects.filter(available=True)
#         if category_slug:
#             category = get_object_or_404(Category, slug=category_slug)
#             products = products.filter(category=category)
#         return render(request, 'store/shop.html', {
#             'category': category,
#             'categories': categories,
#             'products': products})

class ShopProductListView(CatFil, ListView):
    model = Products
    queryset = Products.objects.filter(available=True)
    context_object_name = 'shop'
    template_name = 'store/shop.html'


# class ProductDetailView(View):
#     def get(self, request, id, slug):
#         category = None
#         categories = Category.objects.all()
#         product = get_object_or_404(Products, id=id, slug=slug, available=True)
#         return render(request, 'store/product_detail.html', {'product': product, 'category': category, 'categories': categories,})


class ProductDetailView(CatFil, DetailView):
    form_class = ImageForm
    model = Products
    slug_field = 'slug'
    context_object_name = 'product_detail'
    template_name = 'store/product_detail.html'


""" shop detail view """


class ShopDetailView(View):
    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Products.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'store/detail.html', {'category': category, 'categories': categories, 'products': products})