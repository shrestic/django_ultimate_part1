from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper,DecimalField
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from store.models import Product, Order, Customer


def say_hello(request):
    # Cannot infer type of '*' expression involving these types: DecimalField, FloatField. You must set output_field.
    # queryset = Product.objects.annotate(discounted_price=F("unit_price") * 0.8)
    discounted_price = ExpressionWrapper(F("unit_price") * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discounted_price=discounted_price)

    return render(request, "hello.html", {"name": "Mosh", "result": queryset})
