> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/zhouruifu2015/article/details/129980612?spm=1001.2014.3001.5502)

在前面的DRF系列教程中，以博客为例介绍了序列化器(Serializer), 并使用基于类的视图APIView和ModelViewSet开发了针对文章资源进行增删查改的完整API接口，并详细对权限、认证(含jwt认证)和分页进行了总结与演示。在本篇文章中将向演示如何在Django REST Framework中对分页结果进行进一步过滤和排序。

DRF的过滤是指根据请求参数来筛选数据的功能，例如根据某个字段的值来过滤数据，或者实现一些复杂的查询条件。DRF提供了多种过滤方式，如基于字段的精确匹配、范围过滤、搜索过滤等。

DRF的排序是指对指定字段进行升序或降序排列的功能。DRF支持多字段排序和自定义排序规则。

参考文章：

[3、DRF实战总结：基于类的视图APIView, GenericAPIView和GenericViewSet视图集（附源码）_SteveRocket的博客-CSDN博客](https://blog.csdn.net/zhouruifu2015/article/details/129761752 "3、DRF实战总结：基于类的视图APIView, GenericAPIView和GenericViewSet视图集（附源码）_SteveRocket的博客-CSDN博客")

[4、DRF实战总结：序列化器(Serializer)、数据验证、重写序列化器方法详解（附源码）_SteveRocket的博客-CSDN博客](https://blog.csdn.net/zhouruifu2015/article/details/129965351 "4、DRF实战总结：序列化器(Serializer)、数据验证、重写序列化器方法详解（附源码）_SteveRocket的博客-CSDN博客")

[https://blog.csdn.net/zhouruifu2015/article/details/129965342](https://blog.csdn.net/zhouruifu2015/article/details/129965342 "https://blog.csdn.net/zhouruifu2015/article/details/129965342")

[https://blog.csdn.net/zhouruifu2015/article/details/129965353](https://blog.csdn.net/zhouruifu2015/article/details/129965353 "https://blog.csdn.net/zhouruifu2015/article/details/129965353")

前面教程中当发送GET请求到/v1/articles?page=2时可以得到下面返回的分页数据列表。现在希望对结果进行进一步过滤，比如返回标题含有关键词django的文章资源列表，本文详细总结了如何使用三种方法在Django REST Framework中对返回的响应数据进行过滤和排序。下一篇将开始介绍Django REST Framework的限流和自定义响应数据格式

![](https://img-blog.csdnimg.cn/bac6f676cfd44cd383a253a3d25f7230.png)

DRF的过滤实现方式：DRF提供了FilterBackend接口，可以实现过滤功能。FilterBackend接口包括两个方法：

1. filter_queryset(self, request, queryset, view): 实现具体的过滤逻辑，返回过滤后的queryset对象。
2. get_schema_fields(self, view): 返回用于描述过滤器的元数据。

DRF内置了一些常用的过滤器，如DjangoFilterBackend、SearchFilter、OrderingFilter等，也可以自定义过滤器。

DRF的排序实现方式：DRF提供了OrderingFilter过滤器，可以实现排序功能。OrderingFilter接口继承自FilterBackend，也包括两个方法：

1. filter_queryset(self, request, queryset, view): 实现具体的排序逻辑，返回排序后的queryset对象。
2. get_schema_fields(self, view): 返回用于描述排序方式的元数据。

使用OrderingFilter过滤器时，需要在视图类中定义ordering_fields属性，即允许排序的字段列表。具体使用方式可以参考DRF官方文档。

django-filter是一个Django扩展，提供了方便的过滤数据的功能。它通过定义FilterSet类来实现，可以支持多个过滤条件，包括基于字段的精确匹配、范围过滤、搜索过滤等。django-filter的特点包括：

1. 简单易用：只需要定义FilterSet类并指定需要过滤的字段即可。
2. 定制性强：可以自定义过滤条件和过滤方法。
3. 性能好：通过缓存机制提高过滤性能。
4. 支持复杂查询：可以使用逻辑运算符（与、或、非）来组合多个条件进行复杂查询。

总之，DRF的过滤和排序功能以及django-filter的数据过滤功能可以帮助开发者快速构建强大的API接口，提升数据检索和查询的效率。

**重写GenericsAPIView或viewset的get_queryset方法**
----------------------------------------------

此方法不依赖于任何第三方包, 只适合于需要过滤的字段比较少的模型。比如这里需要对文章title进行过滤，只需要修改ArticleList视图函数类即可。

# drf_pro/views_filter.py

![](https://img-blog.csdnimg.cn/3f5e1bb3bd824fa0b5554a402d2540ac.png)

#drf_pro/urls.py

![](https://img-blog.csdnimg.cn/1bdd5fd812a64da48a8cffefc0a41909.png)

修改好视图类后，发送GET请求到/v1/articles7?q=文章标题, 将得到所有标题含有“文章标题”关键词的文章列表，这里显示一共有1条结果。

![](https://img-blog.csdnimg.cn/14b5f595c173452d8064f475022060ba.png)

当一个模型需要过滤的字段很多且不确定时(比如文章状态、正文等等), 重写get_queryset方法将变得非常麻烦，更好的方式是借助django-filter这个第三方库实现过滤。

**使用django-filter**
-----------------

Django-Filter是一个很好的利用了Django ORM特性，非常好用的第三方库，可以使用很少的代码就扩展原有的接口，实现多种筛选功能。

参考文档：[django-filter · PyPI](https://pypi.org/project/django-filter/ "django-filter · PyPI")

GitHub地址：

[GitHub - carltongibson/django-filter: A generic system for filtering Django QuerySets based on user selections](https://github.com/carltongibson/django-filter "GitHub - carltongibson/django-filter: A generic system for filtering Django QuerySets based on user selections")

![](https://img-blog.csdnimg.cn/f0c19057d2f047ecba3f43725b1a9ae4.png)

[GitHub - carltongibson/django-filter: A generic system for filtering Django QuerySets based on user selections](https://github.com/carltongibson/django-filter "GitHub - carltongibson/django-filter: A generic system for filtering Django QuerySets based on user selections")

 `django-filter`库包含一个 `DjangoFilterBackend`类，该类支持REST框架的高度可定制的字段过滤。推荐使用此过滤方法, 因为它自定义需要过滤的字段非常方便, 还可以对每个字段指定过滤方法(比如模糊查询和精确查询)。具体使用方式如下：

1. 安装django-filter

pip install django-filter

2. INSTALLED_APPS添加django_filters

![](https://img-blog.csdnimg.cn/efb1d46698454c7597b956bc8960ea9a.png)

3. 自定义FilterSet类

这里自定义了按标题关键词和文章状态进行过滤。

# drf_pro/filters.py(新建)

![](https://img-blog.csdnimg.cn/76876929c04647aba2792b660d63bd0c.png)

4. 将自定义FilterSet类加入到View类或ViewSet

另外同时还需要将DjangoFilterBackend设为过滤后台，如下所示：

![](https://img-blog.csdnimg.cn/f9ccbdeb4dca4358bb68a29ef7837074.png)

# drf_pro/urls.py

![](https://img-blog.csdnimg.cn/181afeffd4174a998ca0d2726e1c1ffa.png)

 发送GET请求到/v1/articles8/?q=DRF实战总结&status=p，将得到如下返回结果，只包含发表了的文章。

![](https://img-blog.csdnimg.cn/f4e4fd41b756434fb46db6bfa5ec9e1f.png)

还可以看到REST框架提供了一个新的Filters下拉菜单按钮，可以帮助对结果进行过滤(见上图标红部分)。

**使用DRF提供的SearchFilter类**
---------------------------

DRF自带的具有过滤功能的SearchFilter类，其使用场景与Django-filter的单字段过滤略有不同，更侧重于使用一个关键词对模型的某个字段或多个字段同时进行搜索。

使用这个类，还需要指定search_fields, 具体使用方式如下：

![](https://img-blog.csdnimg.cn/02689a2177b44b29abbfe3a116b3982f.png)

发送GET请求到/v1/articles9/?search=DRF实战总结, 将得到如下结果。

注意：这里进行搜索查询的默认参数名为?search=xxx。

![](https://img-blog.csdnimg.cn/4abd3984694c4b7eb092289c39cd05b7.png)

SearchFilter类非常有用，因为它不仅支持对模型的多个字段进行查询，还支持ForeinKey和ManyToMany字段的关联查询。按如下修改search_fields, 就可以同时搜索标题或用户名含有某个关键词的文章资源列表。修改好后，作者用户名里如果有django，该篇文章也会包含在搜索结果了。

* search_fields = ('title', 'author__username')

默认情况下，SearchFilter类搜索将使用不区分大小写的部分匹配(icontains)。可以在search_fields中添加各种字符来指定匹配方法。

1. '^'开始 - 搜索。
2. '='完全匹配。
3. '@'全文搜索。
4. '$'正则表达式搜索。

例如：search_fields = ('=title', )精确匹配title。

前面详细介绍了对结果进行过滤的3种方法，接下来再看看如何对结果进行排序，这里主要通过DRF自带的OrderingFilter类实现。

**使用DRF的OrderingFilter类**
-------------------------

使用OrderingFilter类首先要把它加入到filter_backends, 然后指定排序字段即可，如下所示：

![](https://img-blog.csdnimg.cn/42304c9ddc4a4e81b1838a6ca8606ccc.png)

发送请求时只需要在参数上加上?ordering=create_date或者?ordering=-create_date即可实现对结果按文章创建时间正序和逆序进行排序。

点击DRF界面上的Filters按钮，还会看到搜索和排序的选项。

![](https://img-blog.csdnimg.cn/50d72890644e493498a1e7cdf070dcb2.png)

**注**：实际开发应用中OrderingFilter类，SearchFilter类和DjangoFilterBackend经常一起联用作为DRF的filter_backends，没有相互冲突。

代码示例：https://download.csdn.net/download/zhouruifu2015/87657280

![](https://img-blog.csdnimg.cn/533706fa6ec2405bb80005d9850d522e.jpeg)

输入才有输出，吸收才能吐纳。——码字不易![](https://img-blog.csdnimg.cn/ba17ede5cb96412c88c9af9fcb5da176.png)
