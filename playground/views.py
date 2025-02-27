from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order
from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # queryset = Product.objects.select_related("collection__someOtherField").all()
    # queryset = Product.objects.prefetch_related("promotions").select_related("collection").all()
    queryset = (
        Order.objects.prefetch_related("orderitem_set__product").select_related("customer").order_by("-placed_at")[:5]
    )

    # return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
    return render(request, "hello.html", {"name": "Mosh", "orders": list(queryset)})
