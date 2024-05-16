"""URLS FOR THE PRODUCTS APP."""

from django.contrib import admin
from django.urls import path

from apps.products.views import home_view, get_product

app_name = "products"
urlpatterns = [
    path('', home_view, name='index-products'),
    path('detail/<int:id>', get_product, name='detail-products'),
]
