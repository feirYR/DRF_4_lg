from rest_framework.permissions import BasePermission

from user.models import User


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        uname=request.data['username']
        user=User.objects.filter(username=uname)
        print(user)
        if user:
            return True
        return False