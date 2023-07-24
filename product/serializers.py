import decimal
from math import floor
from rest_framework import serializers

from .models import Product

from api.serializers import OwnerSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    final_price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'owner',
            'id',
            'name',
            'category',
            'description',
            'discount',
            'price',
            'image',
            'final_price'
        ]

    def get_final_price(self, instance):
        print(instance.price - (
            instance.price * decimal.Decimal(instance.discount / 100)))
        
        return floor(instance.price - (
            instance.price * decimal.Decimal((instance.discount / 100))))
