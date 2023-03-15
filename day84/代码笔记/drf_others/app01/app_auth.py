
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01.models import UserToken
class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 认证逻辑，如果认证通过，返回两个值
        #如果认证失败，抛出AuthenticationFailed异常
        token=request.GET.get('token')
        if  token:
            user_token=UserToken.objects.filter(token=token).first()
            # 认证通过
            if user_token:
                return user_token.user,token
            else:
                raise AuthenticationFailed('认证失败')
        else:
            raise AuthenticationFailed('请求地址中需要携带token')



from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def  has_permission(self, request, view):
        # 不是超级用户，不能访问
        # 由于认证已经过了，request内就有user对象了，当前登录用户
        user=request.user  # 当前登录用户
        # 如果该字段用了choice，通过get_字段名_display()就能取出choice后面的中文
        print(user.get_user_type_display())
        if user.user_type==1:
            return True
        else:
            return False





# 自定义异常处理的方法
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
def my_exception_handler(exc, context):
    response=exception_handler(exc, context)
    # 两种情况，一个是None，drf没有处理
    #response对象，django处理了，但是处理的不符合咱们的要求
    # print(type(exc))

    if not response:
        if isinstance(exc, ZeroDivisionError):
            return Response(data={'status': 777, 'msg': "除以0的错误" + str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'status':999,'msg':str(exc)},status=status.HTTP_400_BAD_REQUEST)
    else:
        # return response
        return Response(data={'status':888,'msg':response.data.get('detail')},status=status.HTTP_400_BAD_REQUEST)


#自己封装Response对象

from rest_framework.response import Response

# return APIResponse(100,'成功',data)

class APIResponse(Response):
    def __init__(self,code=100,msg='成功',data=None,status=None,headers=None,**kwargs):
        dic = {'code': code, 'msg': msg}
        if  data:
            dic = {'code': code, 'msg': msg,'data':data}
        dic.update(kwargs)
        super().__init__(data=dic, status=status,headers=headers)
