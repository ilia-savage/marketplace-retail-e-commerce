import decimal
from math import floor
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

from api.serializers import OwnerSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    final_price = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'owner',
            'id',
            'url',
            'image',
            'get_thumbnail',
            'name',
            'category',
            'description',
            'discount',
            'price',
            'final_price',
            'specs',
        ]

    def get_final_price(self, instance):
        return floor(instance.price - (
            instance.price * decimal.Decimal((instance.discount / 100))))
    

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("model-detail", kwargs={"pk": obj.pk}, request=request)
    
