from . import models
from django.db.models import Count, QuerySet
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.


class InventoryFilter(admin.SimpleListFilter):
    """
    Custom filter for Django admin to filter products based on inventory levels.

    Attributes:
        title (str): The title of the filter displayed in the admin interface.
        parameter_name (str): The parameter name used in the URL query.

    Methods:
        lookups(request, model_admin):
            Returns a list of tuples containing the filter options and their display names.

        queryset(request, queryset: QuerySet):
            Filters the queryset based on the selected filter option.
            If the selected option is "<10", it filters the queryset to include only items with inventory less than 10.
    """

    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request, model_admin):
        return [("<10", "Low")]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


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
        url = reverse("admin:store_product_changelist") + "?" + f"collection__id={collection.id}"
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count("product"))


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ["clear_inventory"]
    # collection__title not work
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    # prevent extra queries (from 15 queries down to 5 queries)
    list_select_related = ["collection"]
    list_filter = ["collection", "last_update", InventoryFilter]
    list_per_page = 10

    def collection_title(self, product: models.Product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product: models.Product):
        if product.inventory < 10:
            return "Low"
        return "OK"

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(request, f"{updated_count} products were successfully updated", level="SUCCESS")


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page = 10
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
    ordering = ["first_name", "last_name"]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
