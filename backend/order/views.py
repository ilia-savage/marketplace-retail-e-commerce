from django.shortcuts import render

from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer
from api.permissions import HasModifyPermission



class OrderListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [HasModifyPermission]