from django.db import models
from product.models import Product
from user.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    phone_number = PhoneNumberField()
    city = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    email = models.EmailField(default=None, null=True)
    products = models.ManyToManyField(Product, through="ProductOrder")

    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductOrder(models.Model):
    product =  models.ForeignKey(Product, null=True, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    # def __str__(self):
    #     return f"Продукт - {self.product.name}, заказ - №{self.order.id}"