from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from store.models import Product, Order, Customer


def say_hello(request):
    # queryset = Customer.objects.annotate(is_new=Value(True))
    queryset = Customer.objects.annotate(is_new=F("id"))

    return render(request, "hello.html", {"name": "Mosh", "result": queryset})
