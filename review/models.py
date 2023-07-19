from django.db import models

from product.models import Product


class Review(models.Model):
    text = models.TextField(max_length=1024)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, null=True, blank=True, choices=(
        (1, "really bad"),
        (2, "bad"),
        (3, 'okay'),
        (4, "good"),
        (5, "great"),
        ))

    def __str__(self):
        return self.product.name
    
