from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from store.models.products import Products, Category


class AuthView(LoginView):
    model = Products
    template_name = 'store/login.html'
    context_object_name = 'home'


class ProductsListView(ListView):
    model = Products
    template_name = 'store/index.html'
    context_object_name = 'product_list'


def home_page(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/index.html', {'category': category, 'categories': categories, 'products': products})