
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve  # django内置给你的一个视图函数
from django.conf import settings  # 以后取配置文件，都用这个
# from drf_day12 import settings
from rest_framework_jwt.views import obtain_jwt_token
from app02 import views
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('order/', views.OrderAPIView.as_view()),
    path('userinfo/', views.UserInfoAPIView.as_view()),
    path('goods/', views.GoodsInfoAPIView.as_view()),
    path('login2/', views.Login2View.as_view({'post':'login'})),

    # 缓存
    path('test/', views.test_cache),
    path('test2/', views.test_cache2)

]
