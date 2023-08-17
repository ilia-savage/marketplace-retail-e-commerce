from django.shortcuts import render

from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer
from api.permissions import HasModifyPermission

from user.auth import get_user



class OrderListAPIVIew(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [HasModifyPermission]

    def get_queryset(self):
        user_id = get_user(self.request)['id']
        qs = Order.objects.filter(user=user_id)

        return qs
    

class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        params = self.request.query_params
        return serializer.save(**params)