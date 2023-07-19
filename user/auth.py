
import jwt, datetime

from django.conf import settings
from .models import User
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class JSONWebTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            payload = jwt.decode(request.COOKIES.get('jwt'), 'secret', algorithms='HS256')
            print(payload)
            user = User.objects.get(id=payload['id'])
        except (jwt.DecodeError, User.DoesNotExist):
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')
        return (user, payload)


def get_user(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise exceptions.AuthenticationFailed('Unauthenticated')
    
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise  exceptions.AuthenticationFailed('Unauthenticated')
    
    return payload