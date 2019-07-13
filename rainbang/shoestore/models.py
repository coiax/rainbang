from decimal import Decimal

from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    image = models.ImageField()

    cost_price = models.DecimalField(max_digits=20, decimal_places=5)
    selling_price = models.DecimalField(max_digits=20, decimal_places=5)

    VAT_CHOICES = [
        (0, "0%"),
        (Decimal("0.20"), "20%"),
    ]

    vat_rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=VAT_CHOICES,
        default=Decimal("0.20"),
        blank=False
    )

    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=255)
    hexcode = models.CharField(max_length=6)

    def __str__(self):
        return "{} ({})".format(self.name, self.hexcode)

class Style(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE,
                             related_name="styles")

    colour = models.ForeignKey(Colour, on_delete=models.CASCADE,
                               related_name="styles")

    # Overrides the shoe's image if present
    image = models.ImageField(blank=True)

    size = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return "Style({},{},{})".format(self.shoe.name, self.colour, self.size)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.TextField(max_length=2000)
    postcode = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name="orders")
    time_placed = models.DateTimeField()

    PLACED = 1
    DISPATCHED = 2
    DELIVERED = 3
    CANCELLED = 4

    STATE_CHOICES = [
        (PLACED, "Placed"),
        (DISPATCHED, "Dispatched"),
        (DELIVERED, "Delivered"),
        (CANCELLED, "Cancelled")
    ]

    state = models.SmallIntegerField(
        choices=STATE_CHOICES,
        default=PLACED,
        blank=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="items")
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
