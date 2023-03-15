from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import  Response
from rest_framework.decorators import action  # 装饰器

from app01.models import Book
from app01.ser import BookSerializer
from rest_framework.request import Request
from rest_framework.authentication import BaseAuthentication

from rest_framework.exceptions import AuthenticationFailed
from app01.app_auth import MyAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from app01 import models

class BookViewSet(ModelViewSet):
    # authentication_classes=[MyAuthentication]
    queryset =Book.objects.all()
    serializer_class = BookSerializer
    # methods第一个参数，传一个列表，列表中放请求方式，
    # ^books/get_1/$ [name='book-get-1'] 当向这个地址发送get请求，会执行下面的函数
    # detail：布尔类型 如果是True
    #^books/(?P<pk>[^/.]+)/get_1/$ [name='book-get-1']
    @action(methods=['GET','POST'],detail=True)
    def get_1(self,request,pk):
        print(request.user.username)
        print(pk)
        book=self.get_queryset()[:2]  # 从0开始截取一条
        ser=self.get_serializer(book,many=True)
        return Response(ser.data)




from rest_framework.authentication import BasicAuthentication
class TestView(APIView):
    def get(self,request):
        print(request.user.username)
        return Response({'msg':'我是测试'})


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