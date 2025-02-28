from django.contrib import admin
from . import models
from django.db.models import Count


# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]
    list_per_page = 10

    # This code below is make ~14 queries for each collection
    # def products_count(self, collection: models.Collection):
    #     return collection.product_set.count()

    # This code is better, make only 1 query for all collections
    # admin.display is a decorator that allows you to define a custom method on the admin class
    @admin.display(ordering="products_count")
    def products_count(self, collection: models.Collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count("product"))


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # collection__title not work
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page = 10
    # prevent extra queries (from 15 queries down to 5 queries)
    list_select_related = ["collection"]

    def collection_title(self, product: models.Product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product: models.Product):
        if product.inventory < 10:
            return "Low"
        return "OK"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
