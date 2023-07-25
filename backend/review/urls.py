from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ReviewCreateAPIView.as_view()),
    path('<str:pk>/', views.ReviewListAPIView.as_view()),
    path('<str:pk>/update/', views.ReviewUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.ReviewDestroyAPIView.as_view()),
]
