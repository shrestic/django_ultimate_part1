from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
from django.db.models import Q, F


def say_hello(request):
    # Products: inventory = price
    # queryset = Product.objects.order_by("unit_price", "-title").reverse()
    product = Product.objects.order_by("unit_price")[0]
    product = Product.objects.latest("unit_price")
    return render(request, "hello.html", {"name": "Mosh", "product": product})
