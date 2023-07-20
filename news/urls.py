from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListAPIView.as_view()),
    path('create/', views.NewsCreateAPIView.as_view()),
    path('<str:pk>/update/', views.NewsUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.NewsDestroyAPIView.as_view()),
]
