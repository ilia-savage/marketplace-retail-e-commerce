import datetime, os

import jwt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.status import HTTP_200_OK
from django.conf import settings

from .serializers import UserSerializer
from .models import User
from .auth import get_user



class RegisterView(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = {}
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            serializer.save()

        data.pop('password')
        return Response(data)
    

class LoginView(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        email = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=email).first()

        if (user is None) or (not user.check_password(password)):
            raise AuthenticationFailed("Incorrect email or password")
        
        payload = {
            'id': user.id,
            'name': user.name,
            'is_staff': user.is_staff,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        print(os.getenv('SECRET'))
        token = jwt.encode(payload, settings.SECRET, algorithm='HS256')
        print(token)

        response = Response()
        response.data = {
            'message': 'success'
        }
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response


class UserView(APIView):
    def get(self, request):
        payload = get_user(request=request)
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class LogoutView(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response