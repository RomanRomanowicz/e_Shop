from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from store.models.products import Products, Category, CategoryGender
from django.views.generic.base import View


class CatGen():
    """categories и gender для вывода """
    def get_category(self):
        return Category.objects.all()

    def get_category_gender(self):
        return CategoryGender.objects.filter(draft=True)


class HomePageView(View):
    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Products.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'store/index.html', {'category': category, 'categories': categories, 'products': products})

















# def home_page(request, category_slug=None, gender_slug=None):
#     category = None
#     gender = None
#     categories = Category.objects.all()
#     genders = CategoryGender.objects.all()
#     products = Products.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     if gender_slug:
#         gender = get_object_or_404(CategoryGender, slug=gender_slug)
#         products = products.filter(gender=gender)
#     return render(request, 'store/index.html', {
#         'category': category,
#         'categories': categories,
#         'genders': genders,
#         'products': products,
#         'gender': gender,
#     }
#                   )