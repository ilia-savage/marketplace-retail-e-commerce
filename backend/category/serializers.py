from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "Category 1"
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'image'
        ]