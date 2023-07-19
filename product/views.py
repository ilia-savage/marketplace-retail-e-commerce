from rest_framework import generics
from rest_framework import permissions

from .models import Product
from .serializers import ProductSerializer
from .permissions import HasModifyPermission

from user.auth import get_user
from user.models import User


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = ()

    '''
    Overriding create method to check if the user is authenticated
    '''

    def perform_create(self, serializer):
        payload = get_user(self.request)

        user = User.objects.get(id=payload['id'])
        return serializer.save(owner=user)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [HasModifyPermission]

    # 
    # def perform_update(self, serializer):
    #     instance = serializer.save()
        # if instance.owner.id == get_user(self.request)['id']
            # return
        # return super().perform_update(serializer)


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [HasModifyPermission]




