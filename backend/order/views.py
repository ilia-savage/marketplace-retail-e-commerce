from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from user.models import User
from product.models import Product

from .serializers import OrderSerializer
from .serializers import ProductOrderSerializer
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

    def create(self, request, *args, **kwargs):
        data = request.data
        """ Taking products field out of data to create ProductOrders"""
        products = data.pop("products")

        if len(products) == 0:
            return Response("No products selected", status=status.HTTP_400_BAD_REQUEST)
        
        user_data = get_user(request)
        user = User.objects.get(id=user_data['id'])

        serializer = OrderSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            order_object = serializer.save(user=user)
            """Insert order id in all products"""
            # for product in products:
            #     product["order"] = order_serializer.data

            for product in products:
                product_order_serializer = ProductOrderSerializer(data=product)
                product_order_serializer.is_valid(raise_exception=True)
                product_order_serializer.save(order=order_object,
                                                product=Product.objects.get(id=product['product']))

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=headers)
