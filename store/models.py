from django.db import models

# Create your models here.


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collections(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)
    collections = models.ForeignKey(Collections, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        ("B", "Bronze"),
        ("S", "Silver"),
        ("G", "Gold"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    """
    The cart field is a ForeignKey linking CartItem to Cart, meaning each CartItem belongs to one Cart, but a Cart can have multiple CartItems.
    on_delete=models.CASCADE: If a Cart is deleted, all related CartItem instances will also be deleted. This makes sense because when a shopping cart is removed, its items should be removed too.
    """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    """
    The product field is a ForeignKey linking CartItem to Product, meaning each CartItem is associated with one Product, but a Product can be in multiple CartItems (i.e., in different carts).
    on_delete=models.PROTECT: This prevents a Product from being deleted if it is referenced in any CartItem. This makes sense because you don’t want to remove a product that customers have in their carts.
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
