from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
#ViewSetMixin:重写了as_view，路由配置变样了， generics.GenericAPIView：只需要配俩东西
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin

from api import ser
from api import models
class RegisterView(GenericViewSet,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset = models.User.objects.all()
    serializer_class =ser.UserModelSerializer

    # 假设get请求和post请求，用的序列化类不一样，如何处理？
    # 重写getget_serializer_class，返回啥，用的序列号类就是啥
    # 注册，用的序列化类是UserModelSerializer，查询一个用的序列化类是UserReadOnlyModelSerializer
    def get_serializer_class(self):
        print(self.action)  # create,retrieve
        if self.action=='create':
            return ser.UserModelSerializer
        elif self.action=='retrieve':
            return ser.UserReadOnlyModelSerializer
        elif self.action=='update':
            return  ser.UserImageModelSerializer