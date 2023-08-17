from rest_framework.serializers import ModelSerializer, ReadOnlyField, ImageField

from .models import Order, ProductOrder
from api.serializers import CategorySerializer


class ProductOrderSerializer(ModelSerializer):
    id = ReadOnlyField(source="product.id")
    name = ReadOnlyField(source="product.name")
    price = ReadOnlyField(source="product.price")
    discount = ReadOnlyField(source="product.discount")
    thumbnail = ImageField(source="product.thumbnail", read_only=True)
    category = CategorySerializer(source="product.category")

    class Meta:
        model = ProductOrder

        fields = [
            'id', 
            'name',
            'price',
            'thumbnail',
            'discount',
            'quantity',
            'category'
            ]
        

class OrderSerializer(ModelSerializer):
    products = ProductOrderSerializer(source="productorder_set", many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
