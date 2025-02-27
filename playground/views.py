from django.shortcuts import render
from django.db import transaction, connection
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from store.models import Collection, OrderItem, Product, Order, Customer
from tags.models import TaggedItem


# @transaction.atomic
def say_hello(request):
    # queryset = Product.objects.raw("SELECT * FROM store_product")
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM store_product")
    # queryset = cursor.fetchall()
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM store_product")
        queryset = cursor.fetchall()

    return render(request, "hello.html", {"name": "Mosh", "result": list(queryset)})
