from collections.abc import Iterable
from django.db import models
from product.models import Product
from django.core.cache import cache

class Ad(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/ads', null=True, blank=True)

    def save(self, *args, **kwargs):
        cache.delete("ad_id")
        cache.delete('ad_product')
        cache.delete('ad_image')
        return super().save(*args, **kwargs)