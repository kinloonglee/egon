"""drf_router_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views

# 第一步：导入routers模块
from rest_framework import routers
# 第二步：有两个类,实例化得到对象
# routers.DefaultRouter 生成的路由更多
# routers.SimpleRouter
router=routers.SimpleRouter()
# 第三步：注册
# router.register('前缀','继承自ModelViewSet视图类','别名')
router.register('books',views.BookViewSet) # 不要加斜杠了

# 第四步
# router.urls # 自动生成的路由,加入到原路由中
# print(router.urls)
# urlpatterns+=router.urls
'''
[
<URLPattern '^books/$' [name='book-list']>, 
<URLPattern '^books/(?P<pk>[^/.]+)/$'[name='book-detail']>
]

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view()),
    path('test/', views.TestView.as_view()),
    # path('books/', views.BookViewSet.as_view({'get':'list','post':'create'})),
    # re_path('books/(?P<pk>\d+)', views.BookViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

]

urlpatterns+=router.urls



'''
SimpleRouter
<URLPattern '^books/$' [name='book-list']>, 
<URLPattern '^books/(?P<pk>[^/.]+)/$'[name='book-detail']>


DefaultRouter
^books/$ [name='book-list']
^books/(?P<pk>[^/.]+)/$ [name='book-detail']  这两条跟simple一样

^$ [name='api-root']  根，根路径会显示出所有可以访问的地址
^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']


^books\.(?P<format>[a-z0-9]+)/?$ [name='book-list']  http://127.0.0.1:8000/books.json
^books/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='book-detail']  http://127.0.0.1:8000/books/1.json


'''