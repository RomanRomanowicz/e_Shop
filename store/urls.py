from django.urls import path, re_path

from store.views.shop_detail_view import shop_detail_view
from store.views.home_view import HomePageView
from store.views.shop_view import ShopProductListView

app_name = 'store'

# Create your views here.
urlpatterns = [
    path('', HomePageView.as_view(), name='product_list'),
    path('shop/', ShopProductListView.as_view(), name='shop'),
    path('shop_detail_view/', shop_detail_view, name='shop_detail_view'),
    path('shop/<slug:category_slug>/', HomePageView.as_view(), name='category_list'),
    path('shop/<int:id>/<slug:category_slug>/', ShopProductListView.as_view(), name='shop_list'),
]