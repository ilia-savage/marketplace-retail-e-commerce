from rest_framework import permissions
from user.auth import get_user
from .models import Product
from user.models import User


class HasModifyPermission(permissions.BasePermission):
    '''
    checks if the authenticated user id is equal to the product owner id
    admins can modify everything
    '''
    def has_permission(self, request, view):
        user_id = get_user(request)['id']
        if (Product.objects.get(id=view.kwargs['pk']).owner.id == user_id or
            User.objects.get(id=user_id).is_staff
            ):
            return True
        return False
