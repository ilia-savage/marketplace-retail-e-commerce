from rest_framework.serializers import ModelSerializer
from .models import News
from api.serializers import OwnerSerializer

class NewsSerializer(ModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = News
        fields = [
            'owner',
            'id',
            'title',
            'description', 
            'full',
            'date',
            'image'
        ]