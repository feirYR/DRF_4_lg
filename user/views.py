from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
# Create your views here.
from user.models import User
from user.serializer import UserModelSerializer
from utils.MyResponse import MyResponse


class UserAPIView(ModelViewSet):
# class UserAPIView(GenericViewSet,RetrieveModelMixin):
    # queryset = User.objects.filter(id=1)
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'
    # lookup_field = 'id'
    def login(self,request,*args,**kwargs):
        input_pwd=request.data['password']
        print(22222,input_pwd)
        try:
            user_ser= self.retrieve(request,*args,**kwargs)
        except:
            return MyResponse(400, '用户名或密码错误')
        pwd = user_ser.data['password']
        if input_pwd == pwd:
            return MyResponse(200, '登陆成功', results=user_ser.data)
        return MyResponse(400, '用户名或密码错误')

    def register(self,request,*args,**kwargs):
        print('注册请求')
        uname=request.data['username']
        user=User.objects.filter(username=uname)
        if user:
            return MyResponse(400, '用户名已存在')
        user_ser = self.create(request, *args, **kwargs)
        return MyResponse(200,'注册成功',results=user_ser.data)

