
from django.db.models import Prefetch, Q

from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from category.models import Category
from .serializers import ProductSerializer
from api.permissions import HasModifyPermission

from user.auth import get_user
from user.models import User


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all().prefetch_related(
        Prefetch('owner', queryset=User.objects.all().only(
            'id', 'username', 'name', 'last_name')))
    serializer_class = ProductSerializer
    authentication_classes = ()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = ()


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    '''
    Overriding create method to check if the user is authenticated
    '''

    def perform_create(self, serializer):
        payload = get_user(self.request)

        user = User.objects.get(id=payload['id'])
        return serializer.save(owner=user)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all().select_related('owner')
    serializer_class = ProductSerializer
    permission_classes = [HasModifyPermission]

    # 
    # def perform_update(self, serializer):
    #     instance = serializer.save()
        # if instance.owner.id == get_user(self.request)['id']
            # return
        # return super().perform_update(serializer)


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all().select_related('owner')
    serializer_class = ProductSerializer
    permission_classes = [HasModifyPermission]


class ProductSearch(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = ()

    def post(self, request):
        query = request.data.get('query', '')

        if query:
            # products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            products = Product.objects.filter(Q(name__icontains=query))

            if products:
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data)

            # category = Category.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            category = Category.objects.filter(Q(name__icontains=query))

            category_ids = [item.id for item in category]

            products = Product.objects.filter(category__in=category_ids)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        
        return Response({"products": []})
    

class ProductListByCategory(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = ()

    def post(self, request):
        if request:
            print(request.data)

            products = Product.objects.filter(category=request.data['category'])
            print(products)
            serializer = ProductSerializer(products, many=True)

            return Response(serializer.data)
        
        return Response({"products": []})