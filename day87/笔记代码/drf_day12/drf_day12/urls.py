"""drf_day12 URL Configuration

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
from django.urls import path,include,re_path
from django.views.static import serve  # django内置给你的一个视图函数
from django.conf import settings  # 以后取配置文件，都用这个
# from drf_day12 import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),  # 路由分发
    path('app02/',include('app02.urls')),
    # 开放media文件
    re_path('media/(?P<path>.*)', serve,{'document_root':settings.MEDIA_ROOT}),

]
