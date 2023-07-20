from rest_framework import permissions
from user.auth import get_user
from product.models import Product
from user.models import User


class HasModifyPermission(permissions.BasePermission):
    '''
    checks if the authenticated user id is equal to the model owner id
    admins can modify everything
    '''
    def has_permission(self, request, view):
        user = get_user(request)
        if (view.queryset.get(id=view.kwargs['pk']).owner.id == user['id'] or
            user['is_staff']
            ):
            return True
        return False
