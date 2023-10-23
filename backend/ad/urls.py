from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdListAPIView.as_view()),
    
]
