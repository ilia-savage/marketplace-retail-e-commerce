from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.core.cache import cache
from .models import Ad
from .serializers import AdSerializer


class AdListAPIView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        ad_cache_id = cache.get("ad_id")
        ad_cache_product = cache.get('ad_product')
        ad_cache_image = cache.get('ad_image')

        if ad_cache_id and ad_cache_product and ad_cache_image:
            return Response({
                "results": {
                    "id": ad_cache_id,
                    "product": ad_cache_product,
                    "image": ad_cache_image,
                }
            })

        response = super().get(request, *args, **kwargs)
        cache.set("ad_id", response.data["results"][0]["id"], 100)
        cache.set("ad_product", response.data["results"][0]["product"], 100)
        cache.set("ad_image", response.data["results"][0]["image"], 100)
        
        return response

    