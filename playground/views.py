from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem
from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # Use only() to restrict the fields retrieved from the database
    queryset = Product.objects.only("id", "title")

    # If 'description' is accessed later, ensure it was included in only() or use defer() carefully
    # queryset = Product.objects.defer("description")  # This is redundant after only()

    return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
