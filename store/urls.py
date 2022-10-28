from django.urls import path, re_path

from store.views.shop_detail_view import shop_detail_view
from store.views.home_view import home_page
from store.views.shop_view import shop_view


app_name = 'store'

# Create your views here.
urlpatterns = [
    path('', home_page, name='product_list'),
    path('shop/', shop_view, name='shop'),
    path('shop_detail_view/', shop_detail_view, name='shop_detail_view'),
    path('<slug:category_slug>/', home_page, name='category_list'),
]