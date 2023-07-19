from rest_framework import serializers

from .models import Product

class OwnerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

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