from rest_framework import generics
from .models import News
from user.auth import get_user
from user.models import User
from .serializers import NewsSerializer
from api.permissions import HasModifyPermission


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = ()


class NewsCreateAPIView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    '''
    Overriding create method to check if the user is authenticated
    '''

    def perform_create(self, serializer):
        payload = get_user(self.request)

        user = User.objects.get(id=payload['id'])
        return serializer.save(owner=user)


class NewsUpdateAPIView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'
    permission_classes = [HasModifyPermission]


class NewsDestroyAPIView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [HasModifyPermission]