from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Shoe, Style

class StyleInline(admin.StackedInline):
    model = Style

class ShoeAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'image_preview',
              ('cost_price', 'selling_price', 'vat_rate'))

    readonly_fields = ["image_preview"]
    inlines = [StyleInline]
    def image_preview(self, shoe):
        fmt = """<img
        style="height: 100%; width: 100%; object-fit: cover;"
        src="{url}" width="{width}" height="{height}">"""
        return mark_safe(fmt.format(
            url=shoe.image.url,
            width=shoe.image.width,
            height=shoe.image.height))

admin.site.register(Shoe, ShoeAdmin)

from .models import Customer
admin.site.register(Customer)

from .models import Order
admin.site.register(Order)

from .models import Colour
admin.site.register(Colour)
