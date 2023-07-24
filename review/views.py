from django.db.models import Prefetch
from rest_framework import generics

from .models import Review
from user.auth import get_user
from user.models import User
from .serializers import ReviewSerializer
from api.permissions import HasModifyPermission
from api.exceptions import ObjectAlreadyExists

from product.models import Product



class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all().prefetch_related(
        'product',
        'owner'
    )
    serializer_class = ReviewSerializer
    lookup_field = 'pk'
    authentication_classes = ()
    '''
    filters reviews that are not related to a particular product
    '''
    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['pk']
        print(pk)
        try:
            product = Product.objects.get(id=pk)
            qs = product.review_set.all()
            print(qs)
        except Product.DoesNotExist:
            return []
        
        return qs


class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    '''
    Overriding create method to check if the user is authenticated
    '''
    def perform_create(self, serializer):
        payload = get_user(self.request)
        user = User.objects.get(id=payload['id'])
        
        """
        Checks if a review already exists for a particular product created
        by authenticated user
        """
        if user.review_set.filter(product=self.request.data['product']):
            raise ObjectAlreadyExists
        return serializer.save(owner=user)


class ReviewUpdateAPIView(generics.UpdateAPIView):
    queryset = Review.objects.all().select_related('owner', 'product')
    serializer_class = ReviewSerializer
    lookup_field = 'pk'
    permission_classes = [HasModifyPermission]


class ReviewDestroyAPIView(generics.DestroyAPIView):
    queryset = Review.objects.all().select_related('owner', 'product')
    serializer_class = ReviewSerializer
    permission_classes = [HasModifyPermission]