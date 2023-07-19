from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    path('<str:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.ProductDestroyAPIView.as_view()),
]
