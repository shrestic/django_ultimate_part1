from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from store.models import Product, Order, Customer


def say_hello(request):
    # queryset = Customer.objects.annotate(
    #     #    full_name= F('first_name') + Value(' ') + F('last_name')
    #     full_name=Func(
    #         F("first_name"),
    #         Value(" "),
    #         F("last_name"),
    #         function="CONCAT",
    #     )
    # )
    queryset = Customer.objects.annotate(
        full_name=Concat("first_name", Value(" "), "last_name")
    )

    return render(request, "hello.html", {"name": "Mosh", "result": queryset})
