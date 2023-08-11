from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrderListCreateAPIVIew.as_view())
]
