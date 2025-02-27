from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from store.models import Collection, OrderItem, Product, Order, Customer
from tags.models import TaggedItem


# SELECT setval('store_order_id_seq', COALESCE((SELECT MAX(id) FROM store_order), 1), true);
# SELECT setval('store_orderitem_id_seq', COALESCE((SELECT MAX(id) FROM store_orderitem), 1), true);


# @transaction.atomic
def say_hello(request):

    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 2
        item.unit_price = 10
        item.save()

        return render(request, "hello.html", {"name": "Mosh"})
