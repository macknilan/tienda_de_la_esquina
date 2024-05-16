from django.http import HttpResponse

from django.shortcuts import render

from apps.products.models import Product


def home_view(request):
    """
    HOME VIEW
    """
    prod = Product.objects.all()

    return render(request, "products/products.html", {"products": prod})


def get_product(request, id):
    """
    GET PRODUCT
    """
    prod = Product.objects.get(pk=id)
    return render(request, "products/product_detail.html", {"product": prod})


