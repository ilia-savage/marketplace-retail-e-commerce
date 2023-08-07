from rest_framework import serializers


class OwnerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)