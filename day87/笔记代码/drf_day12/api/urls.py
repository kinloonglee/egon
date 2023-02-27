
from django.contrib import admin
from django.urls import path,re_path,include
from api import views
from rest_framework.routers import SimpleRouter
router=SimpleRouter()
router.register('register',views.RegisterView,'register')
# 可以注册很多

urlpatterns = [
    # path('register/', views.RegisterView.as_view(action={'post':'create'})),  # 有问题

    path('', include(router.urls)),  # 第二种方式

]

# urlpatterns+=router.urls  # 一种方式
