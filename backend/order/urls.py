from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrderListAPIVIew.as_view()),
    path('create/', views.OrderCreateAPIView.as_view())
]
