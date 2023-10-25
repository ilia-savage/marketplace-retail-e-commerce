from random import randint

from django.shortcuts import render
from django.db.utils import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from user.models import User
from product.models import Product
from user.tasks import send_email

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
    authentication_classes = ()

    def create(self, request, *args, **kwargs):
        data = request.data
        """ Taking products field out of data to create ProductOrders"""
        products = data.pop("products")

        if len(products) == 0:
            return Response("No products selected", status=status.HTTP_400_BAD_REQUEST)
        
        

        """ If user is not registered, we register them ourselves """
        try:
            user_data = get_user(request)
            user = User.objects.get(id=user_data['id'])
        except:
            try:
                # user_data = get_user(request)
                # user = User.objects.get(id=user_data['id'])
                user = User.objects.get(username=data["email"])
                auth_code = str(randint(100000, 999999))
                user.auth_code = auth_code
                print(user, 'df')
                user.save()
                send_email("[ILTECH] - Код для входа в аккаунт", f"Ваш код подтверждения: {auth_code}", user.username)

            except:
                # try:
                auth_code = str(randint(100000, 999999))
                user = User.objects.create(name=data['name'],
                                            last_name=data['last_name'],
                                            username=data['email'],
                                            phone_number=data['phone_number'],
                                            is_active=False,
                                            auth_code=auth_code)
                send_email("[ILTECH] - Код для входа в аккаунт", f"Ваш код подтверждения: {auth_code}")
                    
                # except IntegrityError:
                #     user = User.objects.get(username=data['email'])
                #     send_email("[ILTECH] - Код для входа в аккаунт", f"Ваш код подтверждения: {auth_code}")


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
