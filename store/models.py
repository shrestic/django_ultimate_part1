from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, related_name="+")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)
    promotions = models.ManyToManyField(Promotion)

    def __str__(self):
        return self.title


class Customer(models.Model):
    MEMBERSHIP_FREE = "B"
    MEMBERSHIP_BASIC = "S"
    MEMBERSHIP_PREMIUM = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_FREE, "Bronze"),
        (MEMBERSHIP_BASIC, "Silver"),
        (MEMBERSHIP_PREMIUM, "Gold"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_FREE,
    )

    class Meta:
        db_table = "store_customer"
        indexes = [
            models.Index(fields=["last_name", "first_name"]),
        ]

    def __str__(self):
        return self.email


class Order(models.Model):
    payment_status_PENDING = "P"
    payment_status_COMPLETE = "C"
    payment_status_FAILED = "F"

    payment_status_CHOICES = [
        (payment_status_PENDING, "Pending"),
        (payment_status_COMPLETE, "Complete"),
        (payment_status_FAILED, "Failed"),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=payment_status_CHOICES,
        default=payment_status_PENDING,
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.customer} - {self.placed_at}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.street}"
