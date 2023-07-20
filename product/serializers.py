from rest_framework import serializers

from .models import Product

from api.serializers import OwnerSerializer



class ProductSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'owner',
            'id',
            'name',
            'category',
            'description',
            'price',
            'image',
        ]