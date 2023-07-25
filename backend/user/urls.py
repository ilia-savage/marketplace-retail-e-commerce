from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, Activate

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('', UserView.as_view()), 
    path('logout/', LogoutView.as_view()),
    path('activate/', Activate.as_view())
]
