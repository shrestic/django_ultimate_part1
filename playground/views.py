from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from store.models import Product, Order, Customer
from tags.models import TaggedItem


def say_hello(request):
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects.select_related("tag").filter(
    #     content_type=content_type,
    #     object_id=1,
    # )
    queryset = TaggedItem.objects.get_tags_for(Product, 1)
    return render(request, "hello.html", {"name": "Mosh", "result": list(queryset)})
