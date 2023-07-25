from django.db import models

# Create your models here.
from category.models import Category
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
    specs = models.JSONField(null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"

    def __str__(self):
        return self.name
    

