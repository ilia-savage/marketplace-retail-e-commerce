from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Order, ProductOrder


class ProductOrderSerializer(ModelSerializer):
    id = ReadOnlyField(source="product.id")
    name = ReadOnlyField(source="product.name")
    price = ReadOnlyField(source="product.price")
    discount = ReadOnlyField(source="product.discount")

    class Meta:
        model = ProductOrder

        fields = [
            'id', 
            'name',
            'price',
            'discount',
            'quantity'
            ]
        

class OrderSerializer(ModelSerializer):
    products = ProductOrderSerializer(source="productorder_set", many=True)
    class Meta:
        model = Order
        fields = '__all__'
