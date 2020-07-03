from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from user.models import User


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth=request.META.get('HTTP_AUTHORIZATION',None)
        uname=request.data['username']
        # pwd=request.GET['password']
        # print(uname,pwd)
        print('认证',auth)
        if auth is None:
            return None
        auths=auth.split()
        print(auths)
        if (len(auths)!=2 or auths[0].lower()!='base'):
            print('格式错误',auths[0])
            raise exceptions.AuthenticationFailed('认证信息格式错误')
        if auths[1] != 'yr':
            raise exceptions.AuthenticationFailed('用户认证信息错误')
        # user=User.objects.filter(username=uname,password=pwd)
        # user=User.objects.filter(username=uname)
        user=User.objects.filter(username='xm')
        if user:
            print(type(user))
            return (user,None)
        raise exceptions.AuthenticationFailed('用户不存在')


