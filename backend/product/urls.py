from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
    path('search/', views.ProductSearch.as_view()),
    path('category/', views.ProductListByCategory.as_view()),
    path('<str:pk>/', views.ProductRetrieveAPIView.as_view(), name='model-detail'),
    path('<str:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.ProductDestroyAPIView.as_view()),
]