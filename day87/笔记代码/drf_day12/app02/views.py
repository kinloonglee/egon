from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response
# 使用jwt提供的认证类，局部使用
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# 内置权限类

# 可以通过认证类：JSONWebTokenAuthentication和权限类IsAuthenticated，来控制用户登录以后才能访问某些接口
# 如果用户不登录就可以访问，只需要把权限类IsAuthenticated去掉就可以了
from rest_framework.permissions import IsAuthenticated
class OrderAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication,]
    # 权限控制
    permission_classes = [IsAuthenticated,]
    def get(self,request,*args,**kwargs):
        return Response('这是订单信息')


class UserInfoAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication,]
    # 权限控制
    # permission_classes = [IsAuthenticated,]
    def get(self,request,*args,**kwargs):
        return Response('UserInfoAPIView')




#
from rest_framework_jwt.utils import jwt_response_payload_handler
from app02.utils import MyJwtAuthentication
class GoodsInfoAPIView(APIView):
    authentication_classes = [MyJwtAuthentication,]

    def get(self,request,*args,**kwargs):
        print(request.user)
        return Response('商品信息')


# 手动签发token，完成多方式登录
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, ViewSet

from app02 import ser
# class Login2View(ViewSetMixin,APIView):
class Login2View(ViewSet):  # 跟上面完全一样
    # 这是登录接口
    # def post(self):  # 不写post了，直接写login？
    #     pass

    def login(self, request, *args, **kwargs):

        # 1 需要 有个序列化的类
        login_ser = ser.LoginModelSerializer(data=request.data,context={'request':request})
        # 2 生成序列化类对象
        # 3 调用序列号对象的is_validad
        login_ser.is_valid(raise_exception=True)
        token=login_ser.context.get('token')
        # 4 return
        return Response({'status':100,'msg':'登录成功','token':token,'username':login_ser.context.get('username')})


    # 逻辑在视图类中写

    # def login(self, request, *args, **kwargs):
    #     username=request.data.get('username') # 用户名有三种方式
    #     password=request.data.get('password')
    #     import re
    #     from api import models
    #     from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler
    #     # 通过判断，username数据不同，查询字段不一样
    #     # 正则匹配，如果是手机号
    #     if re.match('^1[3-9][0-9]{9}$',username):
    #         user=models.User.objects.filter(mobile=username).first()
    #     elif re.match('^.+@.+$',username):# 邮箱
    #         user=models.User.objects.filter(email=username).first()
    #     else:
    #         user=models.User.objects.filter(username=username).first()
    #     if user: # 存在用户
    #         # 校验密码,因为是密文，要用check_password
    #         if user.check_password(password):
    #             # 签发token
    #             payload = jwt_payload_handler(user)  # 把user传入，得到payload
    #             token = jwt_encode_handler(payload)  # 把payload传入，得到token
    #            return Response()


# 单页面缓存
from django.views.decorators.cache import cache_page



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


from django.core.cache import cache
# @cache_page(5)  # 缓存5s钟
def test_cache(request):
    p=Person('lqz',18)
    cache.set('name',p)
    import time
    ctime=time.time()
    return render(request,'index.html',context={'ctime':ctime})


def test_cache2(request):

    p=cache.get('name')
    print(type(p))
    print(p.name)
    import time
    ctime = time.time()
    return render(request, 'index.html', context={'ctime': ctime})