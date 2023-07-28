import datetime, os

import jwt

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.status import HTTP_200_OK

from .serializers import UserSerializer
from .models import User
from .auth import get_user
from .tasks import send_email


class RegisterView(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = {}
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            serializer.save(is_active=False)

        user = User.objects.get(username=data['username'])
        confirmation_token = default_token_generator.make_token(user)

        subject = "ILTECH - Email verification"
        message = f"http://127.0.0.1:8000/api/v1/activate/?id={user.id}&token={confirmation_token}"

        send_email.delay(subject, message)

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
        
        print(user.is_active)
        if user.is_active == False:
            raise AuthenticationFailed("User is not verified")
        
        payload = {
            'id': user.id,
            'name': user.name,
            'is_staff': user.is_staff,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        

        token = jwt.encode(payload, os.getenv('SECRET', 'secret'), algorithm='HS256')
        print(token)

        response = Response()
        response.data = {
            'message': 'success'
        }
        response['Access-Control-Allow-Credentials'] = True
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


class Activate(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        id = request.query_params.get('id')
        token = request.query_params.get('token')

        try:
            user = User.objects.get(id=id)
        except(TypeError, ValueError, OverflowError, AttributeError, User.DoesNotExist):
            user = None
        
        if user != None and user.is_active:
            return Response('This account is already verified', status=status.HTTP_400_BAD_REQUEST)
        if user is None:
            return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
        if not default_token_generator.check_token(user, token):
            return Response('Token is invalid or expired', status=status.HTTP_400_BAD_REQUEST)
        
        user.is_active = True
        user.save()
        return Response('Email successfully verified')