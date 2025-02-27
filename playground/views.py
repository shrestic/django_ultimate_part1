from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
from django.db.models import Q


def say_hello(request):
    # Product: inventory < 10 and price < 20
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    
    # Product: inventory < 10 or price < 20
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    

    return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
