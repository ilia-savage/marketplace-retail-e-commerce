from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListAPIView.as_view()),
    path('create/', views.CategoryCreateAPIView.as_view()),
    path('<str:pk>/update/', views.CategoryUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.CategoryDestroyAPIView.as_view()),
]