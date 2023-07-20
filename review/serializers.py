from rest_framework import serializers
from .models import Review
from api.serializers import OwnerSerializer

class ReviewSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    class Meta:
        model = Review
        fields = [
            'owner',
            'id',
            'text',
            'product',
            'rating'
        ]