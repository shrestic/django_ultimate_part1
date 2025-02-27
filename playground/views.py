from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem
from django.db.models import Q, F


def say_hello(request):
    # queryset = Product.objects.value("id", "title", "collection__title")
    # queryset = Product.objects.values_list("id", "title", "collection__title")
    queryset = Product.objects.filter(id__in=OrderItem.objects.values("product_id").distinct()).order_by("title")
    # queryset = OrderItem.objects.values("product_id").distinct()

    return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
