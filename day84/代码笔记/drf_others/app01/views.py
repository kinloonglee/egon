from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from rest_framework.request import Request
from app01 import models
class LoginView(APIView):
    authentication_classes = []
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=models.User.objects.filter(username=username,password=password).first()
        if user:
            # 登陆成功,生成一个随机字符串
            token=uuid.uuid4()
            # 存到UserToken表中
            # models.UserToken.objects.create(token=token,user=user)# 用它每次登陆都会记录一条，不好，如有有记录
            # update_or_create有就更新，没有就新增
            models.UserToken.objects.update_or_create(defaults={'token':token},user=user)
            return Response({'status':100,'msg':'登陆成功','token':token})
        else:
            return Response({'status': 101, 'msg': '用户名或密码错误'})



from app01 import app_auth
# 这个只有超级用户可以访问
class TestView(APIView):
    authentication_classes = [app_auth.MyAuthentication]
    permission_classes = [app_auth.UserPermission]
    def get(self,request,*args,**kwargs):
        return Response('这是测试数据')

# 只要登录用户就可以访问
class TestView2(APIView):
    authentication_classes = [app_auth.MyAuthentication]
    def get(self,request,*args,**kwargs):
        return Response('这是22222222测试数据')


# #演示内置权限，超级管理员可以查看
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
class TestView3(APIView):
    authentication_classes=[SessionAuthentication,]
    permission_classes = [IsAdminUser]
    def get(self,request,*args,**kwargs):
        return Response('这是22222222测试数据，超级管理员可以看')

##解析组件
from rest_framework.parsers import MultiPartParser  #传文件的格式 formdata格式

## 频率限制
from rest_framework.throttling import BaseThrottle




# test4 演示全局未登录用户访问频次
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
class TestView4(APIView):
    authentication_classes=[]
    permission_classes = []
    def get(self,request,*args,**kwargs):
        return Response('我是未登录用户')

# test5 演示局部配置未登录用户访问频次
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.throttling import AnonRateThrottle
from app01.app_auth import MyAuthentication
class TestView5(APIView):
    # authentication_classes=[MyAuthentication]
    permission_classes = []
    throttle_classes = [AnonRateThrottle]
    def get(self,request,*args,**kwargs):
        # 1/0
        return Response('我是未登录用户，TestView5')

# test6 演示登录用户每分钟访问10次，未登录用户访问5次
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.throttling import AnonRateThrottle

from rest_framework.viewsets import  ModelViewSet

class TestView6(APIView):
    authentication_classes = [SessionAuthentication]
    def get(self, request, *args, **kwargs):
        return Response('我是未登录用户，TestView6')

# 过滤组件的使用
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from app01.models import Book
from app01.ser import BookSerializer
class BookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('name','price')

# 排序组件的使用
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from app01.models import Book
from app01.ser import BookSerializer
class Book2View(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ('id', 'price')



#全局异常处理
from rest_framework.views import exception_handler




# 子定制返回对象
from app01.app_auth import APIResponse
class TestView7(APIView):
    def get(self,request,*args,**kwargs):
        return APIResponse(data={"name":'lqz'},token='dsafsdfa',aa='dsafdsafasfdee')