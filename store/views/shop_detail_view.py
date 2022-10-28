from django.shortcuts import render, get_object_or_404
from store.models.products import Products, Category
from django.views.generic import ListView
from store.models.products import Products


def shop_detail_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/detail.html', {'category': category, 'categories': categories, 'products': products})