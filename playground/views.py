from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from store.models import Product
from store.models import Product, Order


def say_hello(request):
    result = Product.objects.filter(collection__id=1).aggregate(
        count=Count("id"),
        min_price=Min("unit_price"),
        max_price=Max("unit_price"),
        avg_price=Avg("unit_price"),
        sum_price=Sum("unit_price"),
    )
    return render(request, "hello.html", {"name": "Mosh", "result": result})
