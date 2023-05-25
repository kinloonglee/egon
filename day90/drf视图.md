> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/zhouruifu2015/article/details/129761752)

前面介绍了什么是符合RESTful规范的API接口，以及使用了基于函数的视图(FBV)编写了对文章进行增删查改的API。在本篇文章将使用基于类的视图(Class-based View, CBV)重写之前的接口。

参考：

[1、Django开发总结：Django MVT与MVC设计模式，请求过程与代码示例（附源码）_SteveRocket的博客-CSDN博客如果要开发一个好的网站或网络应用，就必需了解经典的软件开发所遵循的MVC 设计模式。本篇详细总结软件开发所遵循的MVC (Model-View-Controller, 模型-视图-控制器) 设计模式以及Django的MVT设计模式(Model-View-Template)如何遵循这种设计理念。Django Model(模型), URL(链接), View(视图) 和Template(模板)又是如何遵循MVC软件设计模式的。![](https://g.csdnimg.cn/static/logo/favicon32.ico)https://blog.csdn.net/zhouruifu2015/article/details/129648966](https://blog.csdn.net/zhouruifu2015/article/details/129648966 "1、Django开发总结：Django MVT与MVC设计模式，请求过程与代码示例（附源码）_SteveRocket的博客-CSDN博客")

[https://blog.csdn.net/zhouruifu2015/article/details/129761750![icon-default.png?t=N2N8](https://csdnimg.cn/release/blog_editor_html/release2.2.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N2N8)https://blog.csdn.net/zhouruifu2015/article/details/129761750](https://blog.csdn.net/zhouruifu2015/article/details/129761750 "https://blog.csdn.net/zhouruifu2015/article/details/129761750")

工程路径及APP：django_framework\django_rest_framework_pro\drf_pro

**基于类的视图(CBV)**
-----------------

一个中大型的Web项目代码量通常是非常大的，如果全部使用函数视图写，那么代码的复用率是非常低的。而使用类视图，就可以有效的提高代码复用，因为类是可以被继承的，可以拓展的。特别是将一些可以共用的功能抽象成Mixin类或基类后可以减少重复造轮子的工作。

[DRF](https://so.csdn.net/so/search?q=DRF&spm=1001.2101.3001.7020)推荐使用基于类的视图(CBV)来开发API, 并提供了4种开发CBV开发模式。

* 使用基础APIView类
* 使用Mixins类和GenericAPI类混配
* 使用通用视图generics.*类, 比如generics.ListCreateAPIView
* 使用视图集ViewSet和ModelViewSet

**类视图的比较**
------------

DRF提供了4种编写CBV类API的方式，到底哪种CBV开发模式更好? 答案是各有利弊

* 基础的API类：可读性最高，代码最多，灵活性最高。当需要对API行为进行个性化定制时，建议使用这种方式。
* 通用generics.*类：可读性好，代码适中，灵活性较高。当需要对一个模型进行标准的增删查改全部或部分操作时建议使用这种方式。
* 使用视图集viewset: 可读性较低，代码最少，灵活性最低。当需要对一个模型进行标准的增删查改的全部操作且不需定制API行为时建议使用这种方式。
* mixin类和GenericAPI的混用，这个和generics.*类没什么区别，不看也罢。

Django视图集viewset代码最少，但这是以牺牲了代码的可读性为代价的，因为它对代码进行了高度地抽象化。另外urls由router生成，不如自己手动配置的清楚。

使用CBV类可以简化代码，增加代码重用，在很多情况下还需要重写父类的方法，比如get_queryset, get_serializer_class方法以实现特殊的功能。

**使用APIView类**
-------------

DRF的APIView类继承了Django自带的View类, 一样可以按请求方法调用不同的处理函数，比如get方法处理GET请求，post方法处理POST请求。不过DRF的APIView要强大得多。它不仅支持更多请求方法，而且对Django的request对象进行了封装，可以使用request.data获取用户通过POST, PUT和PATCH方法发过来的数据，而且支持插拔式地配置认证、权限和限流类。

使用APIView类重写之前的函数视图

_# drf_pro/views.py_

```


1.  # 基础APIView类
2.  from rest_framework import status
3.  from rest_framework.views import APIView
4.  from rest_framework.response import Response
5.  from django.http import Http404
6.  from .models import Article
7.  from .serializers import ArticleSerializer2

10.  class ArticleList(APIView):
11.      """
12.      List all articles, or create a new article.
13.      """
14.      def get(self, request, format=None):
15.          articles = Article.objects.all()
16.          serializer = ArticleSerializer2(articles, many=True)
17.          return Response(serializer.data)

19.      def post(self, request, format=None):
20.          serializer = ArticleSerializer2(data=request.data)
21.          if serializer.is_valid():
22.              # 注意：手动将request.user与author绑定
23.              serializer.save(author=request.user)
24.              return Response(serializer.data, status=status.HTTP_201_CREATED)
25.          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

28.  class ArticleDetail(APIView):
29.      """
30.      Retrieve, update or delete an article instance.
31.      """
32.      def get_object(self, pk):
33.          try:
34.              return Article.objects.get(pk=pk)
35.          except Article.DoesNotExist:
36.              raise Http404

38.      def get(self, request, pk, format=None):
39.          article = self.get_object(pk)
40.          serializer = ArticleSerializer2(article)
41.          return Response(serializer.data)

43.      def put(self, request, pk, format=None):
44.          article = self.get_object(pk)
45.          serializer = ArticleSerializer2(instance=article, data=request.data)
46.          if serializer.is_valid():
47.              serializer.save()
48.              return Response(serializer.data)
49.          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

51.      def delete(self, request, pk, format=None):
52.          article = self.get_object(pk)
53.          article.delete()
54.          return Response(status=status.HTTP_204_NO_CONTENT)


```

或许已经注意到，这段代码跟之前基于函数的视图差别并不大。最大不同的是不需要在对用户的请求方法进行判断。该视图可以自动将不同请求转发到相应处理方法，逻辑上也更清晰。

修改url配置, 让其指向新的基于类的视图

_# drf_pro/urls.py_

```


1.  from django.urls import re_path
2.  from rest_framework.urlpatterns import format_suffix_patterns
3.  from . import views, views_cbv

5.  urlpatterns = [
6.      re_path(r'^articles/$', views.article_list),
7.      re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),

9.      # 基于类的视图
10.      re_path(r'^articles_cbv/$', views_cbv.ArticleList.as_view()),
11.      # http://localhost/v1/articles_cbv/

13.      re_path(r'^articles_cbv/(?P<pk>[0-9]+)$', views_cbv.ArticleDetail.as_view()),
14.  ]

16.  urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)


```

发送GET请求到v1/articles_cbv/将看到跟上文一样的效果

![](https://img-blog.csdnimg.cn/bdd3a9386f4442f1beab80258fdd21d1.png)

发送GET请求到v1/articles_cbv/4/ 根据id查看详情

![](https://img-blog.csdnimg.cn/422ad0c737e44c3796075fe2c765a380.png)

**使用Mixin类和GenericAPI类混配**
-----------------------------

使用基础APIView类并没有大量简化代码，与增删改查操作相关的代码包括返回内容对所有模型几乎都是一样的。比如现在需要对文章类别Category模型也进行序列化和反序列化，只需要复制Article视图代码，将Article模型改成Category模型, 序列化类由ArticleSeralizer类改成CategorySerializer类就行了。

对于这些通用的增删改查行为，DRF已经提供了相应的Mixin类。Mixin类可与generics.GenericAPI类联用，灵活组合成所需要的视图。

使用Mixin类和generics.GenericAPI类重写的类视图

_# drf_pro/views.py_

```


1.  # 使用Mixin类和generics.GenericAPI类重写的类视图
2.  from rest_framework import mixins
3.  from rest_framework import generics
4.  class ArticleList2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
5.      """
6.      GenericAPIView 类继承了APIView类，提供了基础的API视图。
7.      """
8.      queryset = Article.objects.all()
9.      serializer_class = ArticleSerializer2

11.      def get(self, request, *args, **kwargs):
12.          return self.list(request, *args, **kwargs)

14.      def post(self, reqeust, *args, **kwargs):
15.          return self.create(reqeust, *args, **kwargs)


```

GenericAPIView 类继承了APIView类，提供了基础的API视图。它对用户请求进行了转发，并对Django自带的request对象进行了封装。不过它比APIView类更强大，因为它还可以通过queryset和serializer_class属性指定需要序列化与反序列化的模型或queryset及所用到的序列化器类。

这里的 ListModelMixin 和 CreateModelMixin类则分别引入了.list() 和 .create() 方法，当用户发送get请求时调用Mixin提供的list()方法，将指定queryset序列化后输出，发送post请求时调用Mixin提供的create()方法，创建新的实例对象。

DRF还提供RetrieveModelMixin, UpdateModelMixin和DestroyModelMixin类，实现了对单个对象实例的查、改和删操作，如下所示：

```


1.  class ArticleDetail2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
2.      queryset = Article.objects.all()
3.      serializer_class = ArticleSerializer2

5.      def get(self, request, *args, **kwargs):
6.          return self.retrieve(request, *args, **kwargs)

8.      def put(self, request, *args, **kwargs):
9.          return self.update(request, *args, **kwargs)

11.      def delete(self, request, *args, **kwargs):
12.          return self.destroy(request, *args, **kwargs)


```

已经有了get, post, delete等方法，为什么mixin类引入的方法要以list, create, retrieve, destroy方法命名?

因为请求方法不如操作名字清晰，比如get方法同时对应了获取对象列表和单个对象两种操作，使用list和retrieve方法后则很容易区分。另外post方法接受用户发过来的请求数据后，有时只需转发不需要创建模型对象实例，所以post方法不能简单等于create方法。

新的ArticleList视图类看似正确，但其实还有一个问题。 定义的序列化器ArticleSeralizer类并不包含author这个字段的，这是因为希望在创建article实例时将author与request.user进行手动绑定。在前面的例子中使用serializer.save(author=request.user)这一方法进行手动绑定。

现在使用mixin类后的操作方法是重写perform_create方法，如下所示：

```


1.  class ArticleList2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
2.      """
3.      GenericAPIView 类继承了APIView类，提供了基础的API视图。
4.      """
5.      queryset = Article.objects.all()
6.      serializer_class = ArticleSerializer2

8.      def get(self, request, *args, **kwargs):
9.          return self.list(request, *args, **kwargs)

11.      def post(self, reqeust, *args, **kwargs):
12.          return self.create(reqeust, *args, **kwargs)

14.      # 将request.user与author绑定
15.      def perform_create(self, serializer):
16.          serializer.save(author=self.request.user)


```

perform_create这个钩子函数是CreateModelMixin类自带的，用于执行创建对象时需要执行的其它方法，比如发送邮件等功能，有点类似于Django的信号。类似的钩子函数还有UpdateModelMixin提供的.perform_update方法和DestroyModelMixin提供的.perform_destroy方法。

urls.py中新定义URL

```


1.  # 使用Mixin类和generics.GenericAPI类重写的类视图
2.  re_path(r'^articles_cbv2/$', views_cbv.ArticleList2.as_view()),
3.  re_path(r'^articles_cbv2/(?P<pk>[0-9]+)/$', views_cbv.ArticleDetail2.as_view()),


```

浏览器请求文章列表

![](https://img-blog.csdnimg.cn/005d357100934d30ab634e30a3f052c6.png)

浏览器请求单篇文章详情

![](https://img-blog.csdnimg.cn/abd66476024b489196cabe157d9a6bec.png)

**使用通用视图generics.*类**
------------------------

将Mixin类和GenericAPI类混配，已经帮助减少了一些代码，但还可以做得更好，比如将get请求与mixin提供的list方法进行绑定感觉有些多余。DRF还提供了一套常用的将 Mixin 类与 GenericAPI类已经组合好了的视图，开箱即用，可以进一步简化的代码，如下所示：

```


1.  from rest_framework import generics
2.  class ArticleList3(generics.ListCreateAPIView):
3.      queryset = Article.objects.all()
4.      serializer_class = ArticleSerializer2
5.      # 将request.user与author绑定
6.      def perform_create(self, serializer):
7.          serializer.save(author=self.request.user)

9.  class ArticleDetail3(generics.RetrieveUpdateAPIView):
10.      queryset = Article.objects.all()
11.      serializer_class = ArticleSerializer2


```

generics.ListCreateAPIView类支持List、Create两种视图功能，分别对应GET和POST请求。generics.RetrieveUpdateDestroyAPIView支持Retrieve、Update、Destroy操作，其对应方法分别是GET、PUT和DELETE。

urls.py中新定义URL

```


1.  # generic class-based views
2.  re_path(r'articles_cbv3/$', views_cbv.ArticleList3.as_view()),
3.  re_path(r'articles_cbv3/(?P<pk>[0-9]+)/$', views_cbv.ArticleDetail3.as_view()),


```

![](https://img-blog.csdnimg.cn/4b42bebf16a444ca8f7a94400029b4ab.png)

![](https://img-blog.csdnimg.cn/d8b239170a1642bb87ad734a0f4f9e45.png)

短短几行代码实现了所有想要的功能，代码更简洁，其它常用generics.*类视图还包括ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView等等。

**使用视图集(viewset)**
-------------------

使用通用视图generics.*类后视图代码已经大大简化，但是ArticleList和ArticleDetail两个类中queryset和serializer_class属性依然存在代码重复。使用视图集可以将两个类视图进一步合并，一次性提供List、Create、Retrieve、Update、Destroy这5种常见操作，这样queryset和seralizer_class属性也只需定义一次就好, 如下所示：

_# drf_pro/views.py_

```


1.  # 视图集(viewset)
2.  from rest_framework import viewsets
3.  class ArticleViewSet(viewsets.ModelViewSet):
4.      # 用一个视图集替代ArticleList和ArticleDetail两个视图
5.      queryset = Article.objects.all()
6.      serializer_class = ArticleSerializer2
7.      # 自行添加，将request.user与author绑定
8.      def perform_create(self, serializer):
9.          serializer.save(author = self.request.user)


```

使用视图集后，需要使用DRF提供的路由router来分发urls，因为一个视图集现在对应多个urls的组合，而不像之前的一个url对应一个视图函数或一个视图类。

_# drf_pro/urls.py_

```


1.  # 使用视图集后，需要使用DRF提供的路由router来分发urls，因为一个视图集现在对应多个urls的组合
2.  from rest_framework.routers import DefaultRouter

4.  router = DefaultRouter()
5.  router.register(r'articles4', viewset=views_cbv.ArticleViewSet)
6.  urlpatterns = [
7.  ]
8.  urlpatterns += router.urls


```

浏览器访问

![](https://img-blog.csdnimg.cn/ece4ab03f2914bcebfa443905be1974b.png)

![](https://img-blog.csdnimg.cn/8801f8a676d74c158ecd5d0ccd1d6570.png)

一个视图集对应List、Create、Retrieve、Update、Destroy这5种操作。有时候只需要其中的几种操作，该如何实现？答案是在urls.py中指定方法映射即可，如下所示：

_# drf_pro/urls.py_

```


1.  from django.urls import re_path
2.  from rest_framework.urlpatterns import format_suffix_patterns
3.  from . import views, views_cbv

5.  # 针对只需要其中的几种操作 使用方法映射
6.  article_list = views_cbv.ArticleViewSet.as_view({
7.      'get': 'list',
8.      'post': 'create'
9.  })
10.  article_detail = views_cbv.ArticleViewSet.as_view({
11.      'get': 'retrieve'  # 只处理get请求，获取单个记录
12.  })

14.  urlpatterns = [
15.      # 视图集(viewset)
16.      re_path(r'^articles5/$', article_list),
17.      re_path(r'^articles5/(?P<pk>[0-9]+)/$', article_detail),
18.  ]


```

另外DRF还提供了ReadOnlyModelViewSet这个类，仅支持list和retrive这个操作。

代码示例：https://download.csdn.net/download/zhouruifu2015/87611605

![](https://img-blog.csdnimg.cn/f82e4ff17be14b7294654395393c4267.jpeg)

输入才有输出，吸收才能吐纳。——码字不易![](https://img-blog.csdnimg.cn/c03bb060a4da4c95b890ae07a3dc8d3b.png)
