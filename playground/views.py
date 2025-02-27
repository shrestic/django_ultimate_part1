from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from store.models import Collection, Product, Order, Customer
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product(pk=1)
    # collection.featured_product_id = 1
    
    # collection = Collection.objects.create(
    #     title="Video Games",
    #     featured_product=Product(pk=1)
    # )
    collection.save()
    return render(request, "hello.html", {"name": "Mosh"})
