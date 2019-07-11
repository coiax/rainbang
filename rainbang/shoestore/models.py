from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    image = models.ImageField(max_length=5243000)

    cost_price = models.DecimalField(max_digits=20, decimal_places=5)
    selling_price = models.DecimalField(max_digits=20, decimal_places=5)
    vat_rate = models.DecimalField(max_digits=7, decimal_places=5)

    def __str__(self):
        return self.name

class Style(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE,
                             related_name="styles")

    colour = models.CharField(max_length=255)
    hexcode = models.CharField(max_length=6)

    # Overrides the shoe's image if present
    image = models.ImageField(max_length=5243000, blank=True)

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
