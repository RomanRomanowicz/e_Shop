from django.shortcuts import render, get_object_or_404
from store.models.products import Products, Category
# from cart.forms import CartAddProductForm


def shop_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/shop.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Products, id=id, slug=slug, available=True)
    # cart_product_form = CartAddProductForm()
    # return render(request, 'store/detail.html', {'product': product, 'cart_product_form': cart_product_form})
    return render(request, 'store/detail.html', {'product': product})