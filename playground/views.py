from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from store.models import Product, Order, Customer


def say_hello(request):
    # order_set not working
    queryset = Customer.objects.annotate(orders_count=Count("order"))

    return render(request, "hello.html", {"name": "Mosh", "result": queryset})
