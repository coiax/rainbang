from django.contrib import admin

from .models import Shoe, Style

class StyleInline(admin.StackedInline):
    model = Style

class ShoeAdmin(admin.ModelAdmin):
    inlines = [StyleInline]

admin.site.register(Shoe, ShoeAdmin)

from .models import Customer
admin.site.register(Customer)

from .models import Order
admin.site.register(Order)

from .models import OrderItem
admin.site.register(OrderItem)
