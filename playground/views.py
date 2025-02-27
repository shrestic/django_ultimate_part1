from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
from django.db.models import Q, F


def say_hello(request):
    queryset = Product.objects.all()[5:10]

    return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
