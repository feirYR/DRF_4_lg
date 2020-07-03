from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
# Create your views here.
from user.authentications import MyAuthentication
from user.permissions import MyPermission
from user.throttle import Mythrottle
from user.models import User
from user.serializer import UserModelSerializer
from utils.Response import MyResponse
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission,IsAuthenticated
from utils.Response import MyResponse

class UserAPIView(ModelViewSet):
# class UserAPIView(GenericViewSet,RetrieveModelMixin):
    # queryset = User.objects.filter(id=1)
    # authentication_classes = [MyAuthentication]
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


class QueryAPIView(APIView):
    # authentication_classes = [MyAuthentication]
    # permission_classes =  [IsAuthenticated]
    # permission_classes =  [MyPermission]
    throttle_classes = [Mythrottle]
    def get(self,request,*args,**kwargs):
        # print(22222)
        # print(111111)
        return Response('游客访问')
    def post(self,request,*args,**kwargs):
        return MyResponse('用户访问')

