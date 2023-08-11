from django.contrib import admin

# Register your models here.

from .models import Order, ProductOrder


admin.site.register(Order)
admin.site.register(ProductOrder)
