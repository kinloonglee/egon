> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.cnblogs.com](https://www.cnblogs.com/abldh12/p/15767580.html)

#### web开发模式

```
# xml,java,python,php,json {"name":"wzh"}
静态页面:没有交互，动态页面:有交互 
```

#### aip接口

```
aip:通过网络规定前后台交互规则，前后台信息交互的媒介 
```

Restful规范
-----------

```
#十条规范
1.数据安全保障，https协议
2.接口特征表现，aip接口
3.多版本数据共存
 	- https://api.baidu.com/v1
    - https://api.baidu.com/v2
4.数据就是资源，均使用名词
	  -	https://api.baidu.com/users
      - https://api.baidu.com/books
      - https://api.baidu.com/book
	一般提倡用资源用复数形式
5.资源请求方式决定(method)
	操作资源:增删改查
        books get:获取所有书
		books/1 get请求，获取主键为1的书
        books post请求 新增一本书
        books/1 put请求，修改主键为1的书
        books/1 patch请求，局部修改主键为1的书
        books/1 delete请求 删除主键为1的书
6.过滤:通过在url上传参数的形式传递搜索文件
    - https://api.example.com/v1/zoos?limit=10:指定返回记录的数量
    - https://api.example.com/v1/zoos?offset=10：指定返回记录的开始位置
 	- https://api.example.com/v1/zoos?page=2&per_page=100：指定第几页，以及每页的记录数
    - https://api.example.com/v1/zoos?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序
    - https://api.example.com/v1/zoos?animal_type_id=1：指定筛选条件
7.响应状态码
	7.1正常响应
    	200：常规请求
    	201：创建成功
    7.2重定向响应
    	301：永久重定向
        302：暂时重定向
    7.3客户端异常
    	403：请求无权限
        404：请求路径不存在
        405：请求方法不存在
    7.4 服务器异常
    	500：服务器异常
8.错误处理，应返回错误信息，error当做key
	{
        error:"无权限操作"
    }
9.返回结果，针对不同操作，服务器用户返回结果应该复合以下规范
	GET/collection 返回资源对象列表(数组)
    GET/collection/resource 返回单个资源对象
    POST/collection 返回新生成的资源对象
    PUT/collection/resourse 返回完整的资源对象
    PATCH/collection/resourse 返回完整的资源对象
    DELETE/collection/resourse 返回一个空文档
10.需要url请求资源需要访问的资源请求链接
    # Hypermedia API，RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么
    {
            "status": 0,
            "msg": "ok",
            "results":[
                {
                    "name":"肯德基(罗餐厅)",
                    "img": "https://image.baidu.com/kfc/001.png"
                }
                ...
                ]
        } 
```

drf简单安装和使用
-----------------

```
#安装 pip install djangorestframework==3.10.3
#使用
	1.在setting.py app注册
      INSTALLED_APPS = [
        'rest_framework'
        ]
	2. 在models.py写表模型
    	class Book(models.Model):
            nid=models.AutoField(primary_key=True)
            name = models.CharField(max_length=32)
            price = models.DecimalField(max_digits=5,decimal_places=2,author=models.CharField(max_length=32))
	3.新建一个序列化
    	from rest_framework.serializers import ModelSerializer 
        from app01.model import Book
        class BookModelSerializer(ModelSerializer):
            class Meta:
                model = Book
                fields = "__all__"
	4.在视图中写视图类
    	from rest_framework.viewsets import ModelViewSet
        from .moddel import Book
        from .ser import BookModelSerializer
        class BooksViewSet(ModelViewSet):
            queryset = Book.object.all()
            serializer_class = BookModelSerializer
	5.写路由关系
    	from app01 import views
        from rest_framework.routers import DefaultRouter
        router = DefaultRouter() # 可以处理视图的路由器
        router.register('book',views.BookViewSet) #向路由器中注册视图集
        	#将路由器中能够所有路由信息追到django的路由列表
            urlpatterns=[
                path('admin/',admin.site.urls)
            ]
        	urlpatterns += router.urls
	6.启动，在postman中测试 
```

源码分析
--------

#### cbv源码分析

```
# ModelViewSet继承View（django原生View）
# APIView继承了View

# 先读View的源码
from django.views import View

# urls.py
path('books1/', views.Books.as_view()),  #在这个地方应该写个函数内存地址,views.Books.as_view()执行完，是个函数内存地址,as_view是一个类方法，类直接来调用，会把类自动传入
放了一个view的内存地址（View--》as_view--》内层函数）

# 请求来了，如果路径匹配，会执行，  函数内存地址(request)
def view(request, *args, **kwargs):
    #request是当次请求的request
    self = cls(**initkwargs)  #实例化得到一个对象，Book对象
    if hasattr(self, 'get') and not hasattr(self, 'head'):
        self.head = self.get
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return self.dispatch(request, *args, **kwargs)

 
def dispatch(self, request, *args, **kwargs):
		#request是当次请求的request   self是book对象
        if request.method.lower() in self.http_method_names:
            #handler现在是：
            handler=getattr(self,'get'),你写的Book类的get方法的内存地址
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)  #执行get(request) 
```

#### API源码分析

```
#from rest_framework.views import APIView
# urls.py
path('booksapiview/', views.BooksAPIView.as_view()),  #在这个地方应该写个函数内存地址

#APIView的as_view方法（类的绑定方法）
   def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)  # 调用父类（View）的as_view(**initkwargs)
        view.cls = cls
        view.initkwargs = initkwargs
        # 以后所有的请求，都没有csrf认证了，只要继承了APIView，就没有csrf的认证
        return csrf_exempt(view)
 

#请求来了---》路由匹配上---》view（request）---》调用了self.dispatch(),会执行apiview的dispatch
  
# APIView的dispatch方法
    def dispatch(self, request, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
        # 重新包装成一个request对象，以后再用的request对象，就是新的request对象了
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?

        try:
            # 三大认证模块
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            # 响应模块
            response = handler(request, *args, **kwargs)

        except Exception as exc:
            # 异常模块
            response = self.handle_exception(exc)

        # 渲染模块
        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response
   
# APIView的initial方法
 	def initial(self, request, *args, **kwargs):
        # 认证组件：校验用户 - 游客、合法用户、非法用户
        # 游客：代表校验通过，直接进入下一步校验（权限校验）
        # 合法用户：代表校验通过，将用户存储在request.user中，再进入下一步校验（权限校验）
        # 非法用户：代表校验失败，抛出异常，返回403权限异常结果
        self.perform_authentication(request)
        # 权限组件：校验用户权限 - 必须登录、所有用户、登录读写游客只读、自定义用户角色
        # 认证通过：可以进入下一步校验（频率认证）
        # 认证失败：抛出异常，返回403权限异常结果
        self.check_permissions(request)
        # 频率组件：限制视图接口被访问的频率次数 - 限制的条件(IP、id、唯一键)、频率周期时间(s、m、h)、频率的次数（3/s）
        # 没有达到限次：正常访问接口
        # 达到限次：限制时间内不能访问，限制时间达到后，可以重新访问
        self.check_throttles(request)
        from rest_framework.request import Request
# 只要继承了APIView，视图类中的request对象，都是新的，也就是上面那个request的对象了
# 老的request在新的request._request
# 以后使用reqeust对象，就像使用之前的request是一模一样（因为重写了__getattr__方法）
  def __getattr__(self, attr):
        try:
            return getattr(self._request, attr) #通过反射，取原生的request对象，取出属性或方法
        except AttributeError:
            return self.__getattribute__(attr)

 # request.data 感觉是个数据属性，其实是个方法，@property，修饰了
	它是一个字典，post请求不管使用什么编码，传过来的数据，都在request.data
 #get请求传过来数据，从哪取？
	request.GET
    @property
    def query_params(self):
        """
        More semantically correct name for request.GET.
        """
        return self._request.GET
  
    #视图类中
     print(request.query_params)  #get请求，地址中的参数
     # 原来在
     print(request.GET) 
```

序列化组件
----------

```
序列化：序列化器把模型对象转换成字典，经过response以后变成json字符串
反序列化，把客户端发送过来的数据，经过request以后变成字典，序列化器把字典转换成模型
3.反序列化，完成数据校验功能 
```

```
步骤
1.写一个序列化类，继承Serializer
2.在类中要写序列化字段，想序列化哪个字段，就在类中写哪个字段
3.在视图类中使用，导入，实例化得到序列化对象，把要序列化的对象传入
4.序列化的对象.data1 是一个字典
5.把字典返回，如果不适用rest_framework 提供的Response ，就得使用JsonResonse

# ser.py
class BookSerializer(serializers.Serializer):
    # id=serializers.CharField()
    name=serializers.CharField()
    # price=serializers.DecimalField()
    price=serializers.CharField()
    author=serializers.CharField()  
    publish=serializers.CharField()
  
# views.py
class BookView(APIView):
    def get(self,request,pk):
        book=Book.objects.filter(id=pk).first()
        #用一个类，毫无疑问，一定要实例化
        #要序列化谁，就把谁传过来
        book_ser=BookSerializer(book)  # 调用类的__init__
        # book_ser.data   序列化对象.data就是序列化后的字典
        return Response(book_ser.data)
  
# urls.py
re_path('books/(?P<pk>\d+)', views.BookView.as_view()), 
```

#### 序列化组件修改数据

```
1 写一个序列化的类，继承Serializer
2 在类中写要反序列化的字段，想反序列化哪个字段，就在类中写哪个字段，字段的属性（max_lenth......）
	max_length	最大长度
    min_lenght	最小长度
    allow_blank	是否允许为空
    trim_whitespace	是否截断空白字符
    max_value	最小值
    min_value	最大值
3.在视图类中使用，导入，实例化得到序列化类的对象，把要修改的对象传入，修改数据传入
4.数据校验 if boo_ser.is_valid()
5.如果校验通过就保存
	boo_ser.save() #book.save
6.如果不通过，自己写
7.字段长度校验规则不够，可以写钩子函数(局部和全局)
	#局部钩子
    def validate_price(self,data)#validate_ + 字段名接收一个参数
     #如果价格小于10，就校验不通过
            # print(type(data))
            # print(data)
            if float(data)>10:
                return data
            else:
                #校验失败，抛异常
                raise ValidationError('价格太低')
	#全局钩子
    def validate(self,validate_data):
        print(validate_data)
    	author=validate_data.get('author')
    	publish=validate_data.get('publish')
        if author == publish:
            raise ValidationError('作者名字和出版社一样')
        else:
            return validate_data
 8. 可以使用字段的author=serializers.CharField(validators=[check_author]) ，来校验
	-写一个函数
    	def check_author(data):
            if data.startswith('sb'):
                raise ValidationError('作者名字不能以sb开头')
            else:
                return data
     -配置：validators=[check_author]     
              
        # models.py
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    author=models.CharField(max_length=32)
    publish=models.CharField(max_length=32)

# ser.py

# from rest_framework.serializers import Serializer  # 就是一个类
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
# 需要继承 Serializer


def check_author(data):
    if data.startswith('sb'):
        raise ValidationError('作者名字不能以sb开头')
    else:
        return data


class BookSerializer(serializers.Serializer):
    # id=serializers.CharField()
    name=serializers.CharField(max_length=16,min_length=4)
    # price=serializers.DecimalField()
    price=serializers.CharField()
    author=serializers.CharField(validators=[check_author])  # validators=[] 列表中写函数内存地址
    publish=serializers.CharField()

    def validate_price(self, data):   # validate_字段名  接收一个参数
        #如果价格小于10，就校验不通过
        # print(type(data))
        # print(data)
        if float(data)>10:
            return data
        else:
            #校验失败，抛异常
            raise ValidationError('价格太低')
    def validate(self, validate_data):   # 全局钩子
        print(validate_data)
        author=validate_data.get('author')
        publish=validate_data.get('publish')
        if author == publish:
            raise ValidationError('作者名字跟出版社一样')
        else:
            return validate_data
    def update(self, instance, validated_data):
        #instance是book这个对象
        #validated_data是校验后的数据
        instance.name=validated_data.get('name')
        instance.price=validated_data.get('price')
        instance.author=validated_data.get('author')
        instance.publish=validated_data.get('publish')
        instance.save()  #book.save()   django 的orm提供的
        return instance

  
 #views.py
class BookView(APIView):
    def get(self,request,pk):
        book=Book.objects.filter(id=pk).first()
        #用一个类，毫无疑问，一定要实例化
        #要序列化谁，就把谁传过来
        book_ser=BookSerializer(book)  # 调用类的__init__
        # book_ser.data   序列化对象.data就是序列化后的字典
        return Response(book_ser.data)
        # return JsonResponse(book_ser.data)

    def put(self,request,pk):
        response_msg={'status':100,'msg':'成功'}
        # 找到这个对象
        book = Book.objects.filter(id=pk).first()
        # 得到一个序列化类的对象
        # boo_ser=BookSerializer(book,request.data)
        boo_ser=BookSerializer(instance=book,data=request.data)

        # 要数据验证（回想form表单的验证）
        if boo_ser.is_valid():  # 返回True表示验证通过
            boo_ser.save()  # 报错
            response_msg['data']=boo_ser.data
        else:
            response_msg['status']=101
            response_msg['msg']='数据校验失败'
            response_msg['data']=boo_ser.errors

        return Response(response_msg)
# urls.py
re_path('books/(?P<pk>\d+)', views.BookView.as_view()), 
```

#### read_only和write_only

```
read_only 表明该字段仅用于序列化输出，默认是False，如果设置成True
postman中可以看到该字段，修改时不需要传该字段
write_only 表示该字段仅用于反序列化输出，默认False 如果设置成
True,postman中看不到该字段，修改时该字段需要传入

required 表示该字段在反序列化时必须输入，默认True
default反序列化时使用默认值
allow_null表示该字段是否允许传入None，默认False
validators 该字段使用的是验证器
error_messages包含错误编号错误信息的字典 
```

#### 查询所有

```
# views.py
class BooksView(APIView):
    def get(self,request):
        response_msg = {'status': 100, 'msg': '成功'}
        books=Book.objects.all()
        book_ser=BookSerializer(books,many=True)  #序列化多条,如果序列化一条，不需要写
        response_msg['data']=book_ser.data
        return Response(response_msg)
  
#urls.py
path('books/', views.BooksView.as_view()), 
```

#### 新增数据

```
# views.py
class BooksView(APIView):

    # 新增
    def post(self,request):
        response_msg = {'status': 100, 'msg': '成功'}
        #修改才有instance，新增没有instance，只有data
        book_ser = BookSerializer(data=request.data)
        # book_ser = BookSerializer(request.data)  # 这个按位置传request.data会给instance，就报错了
        # 校验字段
        if book_ser.is_valid():
            book_ser.save()
            response_msg['data']=book_ser.data
        else:
            response_msg['status']=102
            response_msg['msg']='数据校验失败'
            response_msg['data']=book_ser.errors
        return Response(response_msg)
#ser.py 序列化类重写create方法
    def create(self, validated_data):
        instance=Book.objects.create(**validated_data)
        return instance
# urls.py
path('books/', views.BooksView.as_view()), 
```

#### 删除一个数据

```
# views.py
class BookView(APIView):
    def delete(self,request,pk):
        ret=Book.objects.filter(pk=pk).delete()
        return Response({'status':100,'msg':'删除成功'})
# urls.py
re_path('books/(?P<pk>\d+)', views.BookView.as_view()), 
```

#### 模型类序列化器

```
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book  # 对应上models.py中的模型
        fields='__all__'
        # fields=('name','price','id','author') # 只序列化指定的字段
        # exclude=('name',) #跟fields不能都写，写谁，就表示排除谁
        # read_only_fields=('price',)
        # write_only_fields=('id',) #弃用了，使用extra_kwargs
        extra_kwargs = {  # 类似于这种形式name=serializers.CharField(max_length=16,min_length=4)
            'price': {'write_only': True},
        }
      
# 其他使用一模一样
#不需要重写create和updata方法了 
```

#### many=True实际用途

```
# 序列化多条，需要传many=True
# 
book_ser=BookModelSerializer(books,many=True)
book_one_ser=BookModelSerializer(book)
print(type(book_ser))
#<class 'rest_framework.serializers.ListSerializer'>
print(type(book_one_ser))
#<class 'app01.ser.BookModelSerializer'>

# 对象的生成--》先调用类的__new__方法，生成空对象
# 对象=类名(name=lqz)，触发类的__init__()
# 类的__new__方法控制对象的生成


def __new__(cls, *args, **kwargs):
    if kwargs.pop('many', False):
        return cls.many_init(*args, **kwargs)
    # 没有传many=True,走下面，正常的对象实例化
    return super().__new__(cls, *args, **kwargs) 
```

#### Serializer高级用法

```
#source使用
1.可以该字段名字
 xxx=serializers.CharField(source='title')
2.可以跨表
publish=serializers.CharField(source='publish.email')
3.可以执行方法
pub_date = Serializers.CharField(source='test')
test 是Book表中的方法
#SerializerMethodField()使用
	1.配套方法，方法名叫get_字段名，返回值就是要显示的东西
    authors=serializers.SerializerMethodField()
    def get_authors(self,instance):
        #book对象
        authors = instance.authors.all()
        for author in authors:
              ll=[]
        for author in authors:            						ll.append({'name':author.name,'age':author.age})
        return ll 
```

#### 补充

#### 1 如果有这个错（把rest_framework在app中注册一下）

#### 2补充自己封装Respons对象

```
class MyResponse():
    def __init__(self):
        self.status=100
        self.msg='成功'
    @property
    def get_dict(self):
        return self.__dict__

if __name__ == '__main__':
    res=MyResponse()
    res.status=101
    res.msg='查询失败'
    # res.data={'name':'lqz'}
    print(res.get_dict) 
```

#### 3 你在实际开发中碰到的问题及如何解决的

```
write_only_fields 不能使用了，使用extra_kwargs解决了
extra_kwargs = {
            'id': {'write_only': True},
        } 
```

请求和响应
----------

#### 请求

```
# 请求对象
# from rest_framework.request import Request
    def __init__(self, request, parsers=None, authenticators=None,
                 negotiator=None, parser_context=None):
        # 二次封装request，将原生request作为drf request对象的 _request 属性
        self._request = request
    def __getattr__（self，item）：
    	return getattr(self._request,item)
# 请求对象.data:前端以三种编码方式传入的数据，都可以取出来
# 请求对象..query_params 与Django标准的request.GET相同，只是更换了更正确的名称而已。 
```

#### 响应

```
#from rest_framework.response import Response
 def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
      
#data：你要返回的数据，字典
#status：返回的状态码，默认是200，
	-from rest_framework import status在这个路径下，它把所有使用到的状态码都定义成了常量
#template_name 渲染的模板名字（自定制模板），不需要了解
#headers:响应头，可以往响应头放东西，就是一个字典
#content_type：响应的编码格式，application/json和text/html;

# 浏览器响应成浏览器的格式，postman响应成json格式，通过配置实现的（默认配置）
#不管是postman还是浏览器，都返回json格式数据
# drf有默认的配置文件---》先从项目的setting中找，找不到，采用默认的
# drf的配置信息，先从自己类中找--》项目的setting中找---》默认的找
	-局部使用:对某个视图类有效
        -在视图类中写如下
        from rest_framework.renderers import JSONRenderer
        renderer_classes=[JSONRenderer,]
    -全局使用：全局的视图类，所有请求，都有效
    	-在setting.py中加入如下
        REST_FRAMEWORK = {
            'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
                'rest_framework.renderers.JSONRenderer',  # json渲染器
                'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
            )
        } 
```

视图
----

```
APIView
GenericAPIView 
```

#### 基于APIView写接口

```
#### views.py
from rest_framework.generics import GenericAPIView
from app01.models import Book
from app01.ser import BookSerializer
# 基于APIView写的
class BookView(APIView):
    def get(self,request):
        book_list=Book.objects.all()
        book_ser=BookSerializer(book_list,many=True)

        return Response(book_ser.data)
    def post(self,request):
        book_ser = BookSerializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status':101,'msg':'校验失败'})


class BookDetailView(APIView):
    def get(self, request,pk):
        book = Book.objects.all().filter(pk=pk).first()
        book_ser = BookSerializer(book)
        return Response(book_ser.data)

    def put(self, request,pk):
        book = Book.objects.all().filter(pk=pk).first()
        book_ser = BookSerializer(instance=book,data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})

    def delete(self,request,pk):
        ret=Book.objects.filter(pk=pk).delete()
        return Response({'status': 100, 'msg': '删除成功'})
  
#models.py
class Book(models.Model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    publish=models.CharField(max_length=32)
#ser.py
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
# urls.py
path('books/', views.BookView.as_view()),
re_path('books/(?P<pk>\d+)', views.BookDetailView.as_view()), 
```

#### 基于GenericAPIView写的接口

```
# views.py
class Book2View(GenericAPIView):
    #queryset要传queryset对象，查询了所有的图书
    # serializer_class使用哪个序列化类来序列化这堆数据
    queryset=Book.objects
    # queryset=Book.objects.all()
    serializer_class = BookSerializer
    def get(self,request):
        book_list=self.get_queryset()
        book_ser=self.get_serializer(book_list,many=True)

        return Response(book_ser.data)
    def post(self,request):
        book_ser = self.get_serializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status':101,'msg':'校验失败'})


class Book2DetailView(GenericAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer
    def get(self, request,pk):
        book = self.get_object()
        book_ser = self.get_serializer(book)
        return Response(book_ser.data)

    def put(self, request,pk):
        book = self.get_object()
        book_ser = self.get_serializer(instance=book,data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})

    def delete(self,request,pk):
        ret=self.get_object().delete()
        return Response({'status': 100, 'msg': '删除成功'})
  
 #url.py
    # 使用GenericAPIView重写的
    path('books2/', views.Book2View.as_view()),
    re_path('books2/(?P<pk>\d+)', views.Book2DetailView.as_view()), 
```

#### 基于GenericAPIView写的5个视图扩展类写的接口

```
from rest_framework.mixins import  ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
# views.py
class Book3View(GenericAPIView,ListModelMixin,CreateModelMixin):

    queryset=Book.objects
    serializer_class = BookSerializer
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class Book3DetailView(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset = Book.objects
    serializer_class = BookSerializer
    def get(self, request,pk):
        return self.retrieve(request,pk)

    def put(self, request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
# urls.py
    # 使用GenericAPIView+5 个视图扩展类  重写的
    path('books3/', views.Book3View.as_view()),
    re_path('books3/(?P<pk>\d+)', views.Book3DetailView.as_view()), 
```

#### 使用ModelViewSet编写5个接口

```
# views.py
from rest_framework.viewsets import ModelViewSet
class Book5View(ModelViewSet):  #5个接口都有，但是路由有点问题
    queryset = Book.objects
    serializer_class = BookSerializer
  
# urls.py
# 使用ModelViewSet编写5个接口
    path('books5/', views.Book5View.as_view(actions={'get':'list','post':'create'})), #当路径匹配，又是get请求，会执行Book5View的list方法
    re_path('books5/(?P<pk>\d+)', views.Book5View.as_view(actions={'get':'retrieve','put':'update','delete':'destroy'})), 
```

#### 源码分析ViewSetMixin

```
# 重写了as_view
# 核心代码（所以路由中只要配置了对应关系，比如{'get':'list'}）,当get请求来，就会执行list方法
for method, action in actions.items():
    #method：get
    # action：list
    handler = getattr(self, action)
    #执行完上一句，handler就变成了list的内存地址
    setattr(self, method, handler)
    #执行完上一句  对象.get=list
    #for循环执行完毕 对象.get:对着list   对象.post：对着create 
```

#### 继承ViewSetMixin视图类

```
# views.py
from rest_framework.viewsets import ViewSetMixin
class Book6View(ViewSetMixin,APIView): #一定要放在APIVIew前
    def get_all_book(self,request):
        print("xxxx")
        book_list = Book.objects.all()
        book_ser = BookSerializer(book_list, many=True)
        return Response(book_ser.data)
  
# urls.py
    #继承ViewSetMixin的视图类，路由可以改写成这样
    path('books6/', views.Book6View.as_view(actions={'get': 'get_all_book'})), 
```

路由
----

```
# 在urls.py中配置
	path('books4/',views.Book4View.as_view())
    re_path('books4/(?p<pk>\d+ )')
    views.Book4DetailView.as_view()
#一旦视图类，继承了ViewSetMixin 路由
	path('books5/',views.Book5View.as_view(action={'get':'list','post':'creat'})),# 当路径匹配，又是get请求，会执行Book5View 的list办法
    re_path('books5/(?p<pk>\d+)'),
    view.Book5View.as_view(action={'get':'retrieve','put':'update','delete':'destroy'})
# 继承视图类，ModelViewSet路由写法
	-urls.py
    	#第一步，导入routers模块
        from rest_framework import routers
        # 第二步，有两个类，实例化得到对象
        # routers.DefaultRouter 生成路由更多
        # routers.SimleRouuter 生成少
        # 第三步：注册
        # router.register('前缀'，'继承自ModelViewSet视图类'，'别名')
        router.register('book',views.BookViewSet)# 不需要加斜杠
        #第四步
        router.urls # 自动生成路由
        #print(router.url)
        #urlpatterns += router.urls
	-views.py
    from rest_framework.viewsets import ModelViewSet
    from app01.model import Book
    from app01.ser import BookSerializer
    class BookViewSet(ModelViewSet):
        queryset =Book.objects
        serializer_class = BookSerializer 
```

#### action的使用

```
# action干什么用，为了给继承自ModelViewSet视图类定义函数也添加路由
#使用
calss BookViewSet(ModelViewSet):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    # model 第一个参数，传一个列表，列表中放请求方式
    # ^books/get_1/$ [name='book-get-1'] 当向这个地址发送get请求，会执行下面的函数
    # detail：布尔类型 如果是True
    # ^books/(?p<pk>[^/.]+)/get_1/$[name='book-get-1']
    @action(methods=['GET','POST'],detail=True)
    def get_1(self,request,pk):
        print(pk)
        book = self.get_queryset()[:2]
        ser=self.get_serializer(book,many=True)
        return Response(ser.data) 
```

认证
----

##### 写法

```
#认证实现
	1.写一个类，继承BaseAuthentication，重写1authenticate,认证的逻辑写在里面，认证通过，返回两个值，一个值最终给了Request对象的user，认证失败，抛异常，APIException或者AuthenticationFailed
    2.全局使用，局部 
```

##### 源码分析

```
#1 APIVIew----》dispatch方法---》self.initial(request, *args, **kwargs)---->有认证，权限，频率
#2 只读认证源码： self.perform_authentication(request)
#3 self.perform_authentication(request)就一句话：request.user，需要去drf的Request对象中找user属性（方法） 
#4 Request类中的user方法，刚开始来，没有_user,走 self._authenticate()

#5 核心，就是Request类的 _authenticate(self):
    def _authenticate(self):
        # 遍历拿到一个个认证器，进行认证
        # self.authenticators配置的一堆认证类产生的认证类对象组成的 list
        #self.authenticators 你在视图类中配置的一个个的认证类：authentication_classes=[认证类1，认证类2]，对象的列表
        for authenticator in self.authenticators:
            try:
                # 认证器(对象)调用认证方法authenticate(认证类对象self, request请求对象)
                # 返回值：登陆的用户与认证的信息组成的 tuple
                # 该方法被try包裹，代表该方法会抛异常，抛异常就代表认证失败
                user_auth_tuple = authenticator.authenticate(self) #注意这self是request对象
            except exceptions.APIException:
                self._not_authenticated()
                raise

            # 返回值的处理
            if user_auth_tuple is not None:
                self._authenticator = authenticator
                # 如何有返回值，就将 登陆用户 与 登陆认证 分别保存到 request.user、request.auth
                self.user, self.auth = user_auth_tuple
                return
        # 如果返回值user_auth_tuple为空，代表认证通过，但是没有 登陆用户 与 登陆认证信息，代表游客
        self._not_authenticated() 
```

##### 认证组件使用

```
#写一个认证类 app_auth.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFaild
from app01.models import UserToken
class MyAuthontication(BaseAuthentication):
    def authenticate(self,requset):
        # 认证逻辑，如果认证通过，返回两个值
        # 如果认证失败，抛出抛出AuthenticationFailed异常
        token = request.GET.get('token')
        if token:
            user_token = UserToken.object.filter(token=token).first()
            #认证通过
            if user_token:
                return user_token.user,token
            else:
                raise AuthenticationFaild('认证失败')
		else:
            raise AuthenticationFaild('请求地址中需要携带token')
#可以有多个认证，从左到右一次执行
#全局使用，在setting.py中配置
REST_FRAMEWORK={
    "DEFAULT_AUTHENTICATION_CLASSES":["app01.app_auth.MyAuthentication",]
}
# 局部使用，在视图类上写
authentication_classes = [MyAuthentication]
#局部禁用
authentication_classes=[] 
```

权限
----

##### 源码分析

```
# APIView---->dispatch---->initial--->self.check_permissions(request)(APIView的对象方法)
    def check_permissions(self, request):
        # 遍历权限对象列表得到一个个权限对象(权限器)，进行权限认证
        for permission in self.get_permissions():
            # 权限类一定有一个has_permission权限方法，用来做权限认证的
            # 参数：权限对象self、请求对象request、视图类对象
            # 返回值：有权限返回True，无权限返回False
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request, message=getattr(permission, 'message', None)
                ) 
```

##### 使用

```
# 写一个类继承BasePermission 重写has_permission，如果权限通过，就返回Ture，，不通过就返回False，
from rest_framework.permission import BasePermission
class UserPermission(BasePermission):
    def has_permission(self,request,view):
        # 不是超级用户不能访问，由于认证过了，request有user对象了，是当前登录用户
        user = request.user
         # 如果该字段用了choice，通过get_字段名_display()就能取出choice后面的中文
        print(user.get_user_type_display())
		if user.user_type==1:
            return True
        else:
            return False
      
# 局部使用
class TestView(APIView):
    permission_classes = [app_auth.UserPermission]
  
# 全局使用
在setting中配置
REST_FRAMEWORK={
    "DEFAULT_AUTHENTICATION_CLASSES":["app01.app_auth.MyAuthentication",],
    'DEFAULT_PERMISSION_CLASSES': [
        'app01.app_auth.UserPermission',
    ],
}
# 局部禁用
class TestView(APIView):
    permission_classes = [] 
```

##### 内置权限

```
# 演示一下内置权限的使用：IsAdminUser，控制是否对网站后台有权限的人
# 1 创建超级管理员
# 2 写一个测试视图类
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
class TestView3(APIView):
    authentication_classes=[SessionAuthentication,]
    permission_classes = [IsAdminUser]
    def get(self,request,*args,**kwargs):
        return Response('这是22222222测试数据，超级管理员可以看')
# 3 超级用户登录到admin，再访问test3就有权限
# 4 正常的话，普通管理员，没有权限看（判断的是is_staff字段） 
```

频率
----

##### 内置的频率的限制（限制未登录的用户）

```
#全局使用 限制未登录用户1分钟访问5次
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/m',
    }
}
views.py 里
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SeesionAuthentication,BaseAuthentication
class TestView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,*args,**kwargs):
        return Response('我是未登录用户')
# 局部使用
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.throttling import AnonRateThrottle
class TestView5(APIView):
    authentication_classes = []
    permission_classes = []
    tgrottle_classes = [AnonRateThrottle]
    def get(self,request,*args,**kwargs)
    return Response('我是未登录用户') 
```

##### 内置频率限制登录用户访问频次

```
# 未登录用户一分钟访问5次，登录用户一分钟访问10次
# 需求：未登录用户1分钟访问5次，登录用户一分钟访问10次
全局：在setting中
  'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user': '10/m',
        'anon': '5/m',
    }
      
 局部配置：
UserRateThrottle
class TestView6(APIView):
    authentication_classes=[]
    permission_classes = []
    throttle_classes = [UserRateThrottle]
    def get(self,request,*args,**kwargs):
        return Response('我是未登录用户，TestView6') 
```

过滤
----

```
#1 安装：pip3 install django-filter
#2 注册，在app中注册
#3 全局配，或者局部配
 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
# views.py
class BookView(ListAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    filter_fields = ('name',)#配置可以按照那个字段来过滤 
```

排序
----

```
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from app01.models import Book
from app01.ser import BookSerializer
class Book2View(ListAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ('id','price')
# urls.py
path('books2/',views.Book2View.as_view())

# 使用
http://127.0.0.1:8000/books2/?ordering=-price
http://127.0.0.1:8000/books2/?ordering=price
http://127.0.0.1:8000/books2/?ordering=-id 
```

异常处理
--------

---

```
# 自定义异常处理
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
def my_exception_handler(exc,context):
    response = execption_handler(exc,context)
     # 两种情况，一个是None，drf没有处理
    #response对象，django处理了，但是处理的不符合咱们的要求
    if not response:
        if isinstance(exc,ZeroDivisionError)
        return Response(data={'status':111,'msg':'除以0错误',str(exc)},status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'status':999,'msg':str(exc)},status=status.HTTP_400_BAD_REQUEST)
else:
     return Response(data={'status':888,'msg':response.data.get('detail')},status=status.HTTP_400_BAD_REQUEST)
  
# 全局配置setting.py
'EXCEPTION_HANDLER': 'app01.app_auth.my_exception_handler', 
```

封装对象
--------

```
class APIResponse(Response):
    def __init__(self,code=100,msg='成功',data=None,status=None,headers=None,**kwargs):
        dic = {'code':code,'msg':msg}
        if data:
            dic = {'code':code,'msg':msg,'data':data} 
```

book系列表的接口
----------------

```
# urls.py
from django.urls import path,re_path
from api import views
urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    re_path('books/(?P<pk>\d+)', views.BookAPIView.as_view()),
]
# views.py
from rest_framework.response import Response
from api import models
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from api.ser import BookModelSerializer
class BookAPIView(APIView):
    def get(self,request,*args,**kwargs):
        # 查所有
        book_list = models.Book.objects.all().filter(is_delete=False)
        book_list_ser = BookModelSerlizer(book_list,many=True) 
        # 查一个
        # 同上,查询单个和查询多个合到了一起
	def post(self,request,*args,**kwargs):
        #具备增单条环绕增多条功能
        if isinstance(request.data,dict):
            book_ser = BookModelSerializer(data=request.data)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
        elif isinstance(request.data,list):
            # 现在book_ser是ListSerializer对象
            from rest_framework.serializer import ListSerializer
            book_ser = BookModelSerializer(data=request.data,many=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
	def create(self,validated_data):
        self.child是BookModelSerializer对象
        return [
            self.child.create(attrs) for attrs in validated_data
        ]
    def put(self,request,*args,**kwargs):
        if kwargs.get('pk',None):
            book = model.Book.objects.filter(pk=kwargs.get('pk')).first()
    	    book_ser = BookModelSerializer(instance=book,data=request.data,partial=True) # 增多条
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
        else:
            #改多个
            book_list = []
            modify_data=[]
   
            for item in request.data:
                pk = item.pop('id')
                book = model.Book.objects.get(pk=pk)
                book_list.append(book)
                modify_data.append(item)
	 # 第一种是利用for循环一个个修改
    for i,si_data in enumerate(modify_data)
    	book_ser = BookModelSerializer(instance=book_list[i],data=si_data)
    	book_ser.is_valid(raise_exception=True)
        book_ser.save()
        return Response(data='成功')
    #第二种方案 ,重写ListSerializer 的update方法
      book_ser = BookModelSerializer(instance=book_list,data=modify_data,many=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()  #ListSerializer的update方法,自己写的update方法
    	return Response(book_ser.data)
	def delete(self,request,*args,**kwargs):
        #单个删除批量删除
        pk = kwargs.get('pk')
        pks = []
        if pk:
            #单条删除
            pks.append(pk)
            # 不管删除单条还是多条，都用多条删除
		else:
            pks = request.data.get('pks')
		# 把is_delete改为true
        # ret返回影响行数
        ret = model.Book.object.filter(pk__in=pks,is_delete=False).update(is_delete=True)
        if ret:
            return Response(data={'msg':'删除成功'})
        else:
            return Response(data={'msg':'没有要删除的数据'})
# ser.py
from rest_framework import serializers
from api import models
# 写一个类继承ListSerializer,重写update
class BookListSerializer(serializers.ListSerializer):
    def create(self,validated_data):
        return super().create(validated_data)
    def update(self,instance,validated_data):
        # 保存数据
        # self.child是BookModelSerializer对象
        ll = []
        for i,si_data in enumerate(validated_data):
            ret = self.child.update(instance[i],si_data)
            ll.append(ret)
		return [self.child.update(对象，字典)for attrs in validated_data
                self.child.update(instance[i],attrs) for i,attrs in 				enumerate(validated_data]                                     
# 如果序列化的是数据库的表，尽量用ModelSerializer
class BookModelSerializer(serializer.ModelSerializer)
	class Meta:
	list_serializer_class = BookListSerializer
 	model = model.Book
    firlds =('name','price','authors','publish','publish_name','author_list')
    extra_kwargs={
        'publish':{'write_only':True},
        'publish_name':{'read_only':True},
        'authors':{'write_only':True},
        'author_list':{'read_only':True}
                 } 
```

```
# models.py   

from django.db import models
from django.contrib.auth.models import AbstractUser
class BaseModel(models.Model):
    is_delete = mdoels.BooleanField(default=False)
    # auto_now_add=True 只要记录创建，不需要手动插入时间，自动把当前时间插入
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now=True,只要更新，就会把当前时间插入
	last_update_time = mdoels.DateTimeField(auto_now=True)
    import datetime
    create_time = models.DateTimeField(default=datetime.datetime.now)
    class Meta:
        # 单个字段，有索引，有唯一
        # 多个字段，有联合索引，联合唯一
        abstract = True # 抽象表，不再建立数据库
      
class Book(BaseModel):
    id = models.AutoField(primary_key=True)
    # verbose_name admin 中显示中文
    name = mdoels.CharField(max_length=32,verbose_name='书名',help_text='写书名')
    price = models.DecimalField(max_digiits=5,decimal_places=2)
    # 一对多关系一旦确立，关联字段写在多的一方
    # to_field 默认不写，关联到Publish主键
    # db_constraint = False 逻辑上的关联，实质上没有外键联系，增删不会受到外键影响，但是orm查询不受影响,db_constraint=False,这个就是保留跨表查询的便利(双下划线跨表查询```),但是不用约束字段了,一般公司都用false,这样就省的报错,因为没有了约束(Field字段对象,既约束,又建立表与表之间的关系)
    publish = models.Foreignkey(to='publish',on_delete=models.DO_NOTHING,db_constraint=False)
 # 多对多，跟作者，关联字段，查询次数多的一方
# 第三张表只有关联字段，用自动；第三张表有扩展字段，需要手写，，不能写on_delete
author=models。ManyToManyField(to='Author',db_constraint=False)
class Meta:
    verbose_name_plural='书表'
    def __str__(self):
        return self.name
    @property
    def publish_name(self):
        return self.publisih.name
    def author_list(self):
        author_list = self.authors.all()
        ll = []
        for author in author_lsit:
            ll.append({'name':author.name,'sex':author.get_sex_display()})
            return ll
         return [ {'name':author.name,'sex':author.get_sex_display()}for author in author_list]
  

class Publish(BaseModel):
    name = models.CharField(max_length=32)
    addr = model.CharField(max_length=32)
    def __str__(self):
        return self.name
class Author(BaseModel):
    name = models.ChaeField(max_length=32)
    sex=models.IntegerField(choices=((1,'男'),(2,'女')))
    # 一对一关系卸载查询率高的一方
    authordetail = models.OneToOneField(to='AuthorDetail',db_constraint=False,on_delete=models.CASCADE)

class AuthorDetail(BaseModel):
    mobile=models.CharField(max_length=11)
  
# 二、表断关联
# 1、表之间没有外键关联，但是有外键逻辑关联(有充当外键的字段)
# 2、断关联后不会影响数据库查询效率，但是会极大提高数据库增删改效率（不影响增删改查操作）
# 3、断关联一定要通过逻辑保证表之间数据的安全，不要出现脏数据，代码控制
# 4、断关联
# 5、级联关系
#       作者没了，详情也没：on_delete=models.CASCADE
#       出版社没了，书还是那个出版社出版：on_delete=models.DO_NOTHING
#       部门没了，员工没有部门(空不能)：null=True, on_delete=models.SET_NULL
#       部门没了，员工进入默认部门(默认值)：default=0, on_delete=models.SET_DEFAULT 
```

分页器
------

```
# views.py
#查所有才需要分页
from rest_framework.generics import ListAPIView
#内置分页
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPaination

class MyPageNumberPageination(PageNumberPagination):
    page_size = 3 # 每页条数
    page_query_param = 'aaa' #查询第几页key
    page_size_query_param = 'size' # 每一页条数
    max_page_size = 5

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3 # 每页条数
    limit_query_param = 'limit' # 往后取几条
    offset_query_param = 'offset' #标杆
    max_limit = 5 #每页最大几条
class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'# 每一页查询key
    page_size = 2 #每页显示的条数
    ordering = 'id' 或 '-id' #排序字段

 class BookView(ListAPIView):
     # queryset = models.Book.objects.all().filter(is_delete=False)
     queryset = models.Book.objects.all()
     serializer_class = BookModelSerializer
     #配置分页
     pagination_class = MyCursorPagination

# 使用APIView 分页
from utils.throtting import MyThrottle
class BookView(APIView):
	def get(self,request,*args,**kwargs):
        book_list = models.Book.objecta.all()
        # 实例化得到一个分页器的对象
        page_cursor = MyPageNumberPagination()
        book_list = page_cursor.paginate_querset(book_list,request,view=self)
        next_url = page_cursor.ge_next_link()
        pr_url = page_cursor.get_previous_link()
        book_ser = BookModelSerializer(book_list,many=True)
        return Response(data=book_ser.data)
#settings.py
REST_FRAMEWORK={
    'PAGE_SIZE': 2,
} 
```

根据ip进行频率限制
------------------

```
# 写一个类继承继承SimpleRateThrottle,只要重写get_cache_key
from rest_framework.throttling import ScopedRateThrottle,SimpleRateThrottle
# 继承SimpleRateThrottle
class MyThrottle(SimpleRateThrottle):
    scope='lufei'
    def get_cache_key(self,request,view)
    retrn request.META.get('REMOTE_ADDR')

# 局部使用，全局使用
REST_FRAMEWORK={
    'DEFAULT_THROTTLE_CLASSES': (
        'utils.throttling.MyThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'luffy': '3/m'  # key要跟类中的scop对应
    },
} 
```

自定制频率
----------

```
# 自定制频率，需要两个方法
#判断是否限次，没有限次可以请求True，限次不可以请求False
#限次后调用，显示还需要等待多长时间才能访问，返回需要等待时间seconds

import time
class IPThrottle():
     #定义成类属性,所有对象用的都是这个
    VISIT_DIC = {}
    def __init__(self):
        self.history_list=[]
    def allow_request(self, request, view):
        1.取出访问者的ip
        2.判断在不在访问字典里，不在就添加进去，并返回True，表示第一次访问，在字典里，continue
        3.循环当前的ip表，当前时间减去列表最后一格时间大于60s，把这种数据pop掉，列表里只有60s以内的
        4.当列表小于3说明一分钟不足三次，把当前时间插入到列表第一个位置，返回True
        5.当大于等于3，说明一分钟访问超过3次，返回False验证失败
        ip=request.META.get('REMOTE_ADDR')
        ctime=time.time()
        if ip not in self.VISIT_DIC:
            self.VISIT_DIC[ip]=[ctime,]
            return True
        self.history_list=self.VISIT_DIC[ip]
        while True:
            if ctime-self.history_list[-1]>60:
                self.history_list.pop()
            else:
                break
		if len(self.history_list)<3:
            self.history_lsit.insert(0,ctime)
            return True
        else:
            return False
	def wait(self):
        # 当前时间，减去列表中最后一个时间
        ctime = time.time()
        return 60-(ctime-self.history_list[-1]) 
```

##### Simpleratethrottle源码分析

```
# SimpleRateThrottle源码分析
    def get_rate(self):
        """
        Determine the string representation of the allowed request rate.
        """
        if not getattr(self, 'scope', None):
            msg = ("You must set either `.scope` or `.rate` for '%s' throttle" %
                   self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        try:
            return self.THROTTLE_RATES[self.scope]  # scope：'user' => '3/min'
        except KeyError:
            msg = "No default throttle rate set for '%s' scope" % self.scope
            raise ImproperlyConfigured(msg)
    def parse_rate(self, rate):
        """
        Given the request rate string, return a two tuple of:
        <allowed number of requests>, <period of time in seconds>
        """
        if rate is None:
            return (None, None)
        #3  mmmmm
        num, period = rate.split('/')  # rate：'3/min'
        num_requests = int(num)
        duration = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[period[0]]
        return (num_requests, duration)
    def allow_request(self, request, view):
        if self.rate is None:
            return True
        #当前登录用户的ip地址
        self.key = self.get_cache_key(request, view)  # key：'throttle_user_1'
        if self.key is None:
            return True

        # 初次访问缓存为空，self.history为[]，是存放时间的列表
        self.history = self.cache.get(self.key, [])
        # 获取一下当前时间，存放到 self.now
        self.now = self.timer()

        # Drop any requests from the history which have now passed the
        # throttle duration

        # 当前访问与第一次访问时间间隔如果大于60s，第一次记录清除，不再算作一次计数
        # 10 20 30 40
        # self.history:[10:23,10:55]
        # now:10:56
        while self.history and  self.now - self.history[-1] >= self.duration:
            self.history.pop()

        # history的长度与限制次数3进行比较
        # history 长度第一次访问0，第二次访问1，第三次访问2，第四次访问3失败
        if len(self.history) >= self.num_requests:
            # 直接返回False，代表频率限制了
            return self.throttle_failure()

        # history的长度未达到限制次数3，代表可以访问
        # 将当前时间插入到history列表的开头，将history列表作为数据存到缓存中，key是throttle_user_1，过期时间60s
        return self.throttle_success() 
```

自动生成接口文档
----------------

```
# 1 安装：pip install coreapi

# 2 在路由中配置
	from rest_framework.documentation import include_docs_urls
    urlpatterns = [
        ...
        path('docs/', include_docs_urls(title='站点页面标题'))
    ]
#3 视图类：自动接口文档能生成的是继承自APIView及其子类的视图。
	-1 ） 单一方法的视图，可直接使用类视图的文档字符串，如
        class BookListView(generics.ListAPIView):
            """
            返回所有图书信息.
            """
    -2)包含多个方法的视图，在类视图的文档字符串中，分开方法定义，如
        class BookListCreateView(generics.ListCreateAPIView):
            """
            get:
            返回所有图书信息.
            post:
            新建图书.
            """
    -3)对于视图集ViewSet，仍在类视图的文档字符串中封开定义，但是应使用action名称区分，如
        class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
        """
        list:
        返回图书列表数据
        retrieve:
        返回图书详情数据
        latest:
        返回最新的图书数据
        read:
        修改图书的阅读量
        """ 
```

JWT认证
-------

```
jwt=Json Web token
#原理
"""
1）jwt分三段式：头.体.签名 （head.payload.sgin）
2）头和体是可逆加密，让服务器可以反解出user对象；签名是不可逆加密，保证整个token的安全性的
3）头体签名三部分，都是采用json格式的字符串，进行加密，可逆加密一般采用base64算法，不可逆加密一般采用hash(md5)算法
4）头中的内容是基本信息：公司信息、项目组信息、token采用的加密方式信息
{
	"company": "公司信息",
	...
}
5）体中的内容是关键信息：用户主键、用户名、签发时客户端信息(设备号、地址)、过期时间
{
	"user_id": 1,
	...
}
6）签名中的内容时安全信息：头的加密结果 + 体的加密结果 + 服务器不对外公开的安全码 进行md5加密
{
	"head": "头的加密字符串",
	"payload": "体的加密字符串",
	"secret_key": "安全码"
}
"""

校验
"""
1）将token按 . 拆分为三段字符串，第一段 头加密字符串 一般不需要做任何处理
2）第二段 体加密字符串，要反解出用户主键，通过主键从User表中就能得到登录用户，过期时间和设备信息都是安全信息，确保token没过期，且时同一设备来的
3）再用 第一段 + 第二段 + 服务器安全码 不可逆md5加密，与第三段 签名字符串 进行碰撞校验，通过后才能代表第二段校验得到的user对象就是合法的登录用户
"""

drf项目的jwt认证开发流程（重点）
"""
1）用账号密码访问登录接口，登录接口逻辑中调用 签发token 算法，得到token，返回给客户端，客户端自己存到cookies中

2）校验token的算法应该写在认证类中(在认证类中调用)，全局配置给认证组件，所有视图类请求，都会进行认证校验，所以请求带了token，就会反解出user对象，在视图类中用request.user就能访问登录的用户

注：登录接口需要做 认证 + 权限 两个局部禁用
"""

# 第三方写好的  django-rest-framework-jwt
# 安装pip install djangorestframework-jwt

# 新建一个项目，继承AbstractUser表（）

# 创建超级用户

# 简单使用
 #urls.py
    from rest_framework_jwt.views import ObtainJSONWebToken,VerifyJSONWebToken,RefreshJSONWebToken,obtain_jwt_token
    path('login/', obtain_jwt_token), 
```

自定制auth认证类
----------------

```
from rest_framework_jwt.authentication import BaseAuthentication,BaseJSONWebTokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.authentication import get_authorization_header,jwt_get_username_from_payload
from rest_framework import exceptions
class MyToken(BaseJSONWebTokenAuthentication):
    def authenticate(self,request):
        jwt_value=str(request.META.get('HTTP_AUTHORIZATION'))
        try:
            payload = jwt_decode_handler(jwt_value)
		except Exception:
            raise exception.AuthenticationFaild('认证失败')
            user = slef.authenticate_credentials(payload)
		return user,None 
```

jwt
---

---

##### 控制用户登录后才能访问，不登录也能访问

```
#登录才能访问
from rest_framework.permissions import IsAuthenticated
class OrderAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    # 权限控制
    permission_classes = [IsAuthenticated,]
    def get(self,request,*args,**kwargs):
        return Response('这是订单信息，登录访问')
# 不登录就可以访问
class UserInfoAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    #权限控制
    #  permission_classes = [IsAuthenticated,]
     def get(self,request,*args,**kwargs):
        return Response('这，不登录也能访问') 
```

##### 控制登录接口返回的数据格式

```
# 控制登录接口返回的数据格式
	第一种方案，字节写登录接口
    第二种，用内置，控制登录接口返回的数据格式
        	-jwt的配置信息中有这个属性
    	    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',
    	-重写jwt_response_payload_handler，配置成咱们自己的 
```

##### 自定义基于jwt的权限类

```
#自定义基于jwt权限类
from rest_framework.authentication import BaseAuthentication  # 基于它
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication # 基于它
from rest_framework.exceptions import AuthenticationFailed
# from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.utils import jwt_decode_handler # 跟上面是一个
import jwt

from api import models
class MyJwtAuthentication(BaseAuthentication):
    def authenticate(self,request):
        jwt_value = request.META.get('HTTP_AUTHORIZATION')
 class MyJwtAuthentication(BaseAuthentication):
     def authenticate(self, request):
         jwt_value=request.META.get('HTTP_AUTHORIZATION')
         if jwt_value:
             try:
             #jwt提供了通过三段token，取出payload的方法，并且有校验功能
                 payload=jwt_decode_handler(jwt_value)
             except jwt.ExpiredSignature:
                 raise AuthenticationFailed('签名过期')
             except jwt.InvalidTokenError:
                 raise AuthenticationFailed('用户非法')
             except Exception as e:
                 # 所有异常都会走到这
                 raise AuthenticationFailed(str(e))
             # 因为payload就是用户信息的字典
             print(payload)
             # return payload, jwt_value
             # 需要得到user对象，
             # 第一种，去数据库查
             # user=models.User.objects.get(pk=payload.get('user_id'))
             # 第二种不查库
             user=models.User(id=payload.get('user_id'),username=payload.get('username'))
             return user,jwt_value
         # 没有值，直接抛异常
         raise AuthenticationFailed('您没有携带认证信息')
class MyJwtAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        jwt_value=request.META.get('HTTP_AUTHORIZATION')
        if jwt_value:
            try:
            #jwt提供了通过三段token，取出payload的方法，并且有校验功能
                payload=jwt_decode_handler(jwt_value)
            except jwt.ExpiredSignature:
                raise AuthenticationFailed('签名过期')
            except jwt.InvalidTokenError:
                raise AuthenticationFailed('用户非法')
            except Exception as e:
                # 所有异常都会走到这
                raise AuthenticationFailed(str(e))
            user=self.authenticate_credentials(payload)
            return user,jwt_value
        # 没有值，直接抛异常
        raise AuthenticationFailed('您没有携带认证信息') 
```

##### 手动签发token（多方式登录）

```
# 使用用户名手机号邮箱都可以登录
views.py
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, ViewSet

from app02 import ser
class Login2View(ViewSet):
    def login(self,request,*args,**kwargs):
        1.需要有一个序列化类
        login_ser = ser.LoginModelSerializer(data=request.data,context={'request':request})
        2.生成序列化类对象
        3.调用序列号对象的is_valid
        login_ser.is_valid(raise_exception=True)
        token=login_ser.context.get('token')
        4.return
    return Response({'status':100,'msg':'登陆成功','token'：token，})
from rest_framework import serializers
from api import models
from rest_framework.execptions import ValidationError
from rest_framework_jwt.utils import jwt_encode_handler,jwt_payload_handler
class LoginModelSerializer(serializer.ModelSerializer):
    username = serializer.CharField()
    # 重新覆盖username字段，数据中它是unique,post,认为你是保存数据，自己校验过
    class META:
        mdoel = models.User
        fields=['username','password']
        def validate(self,attrs):
            # 在这里写逻辑
            username = attrs.get('username')
            password = attrs.get('password')
            if re.match('^1[3-9][0-9]{9}$',username): #手机号
                user = models.User.object.filter(mobile=username).first()
            elif re.match('^.+@.+$',username): #邮箱
                user = mobile.User.object.filter(email=username).first()
            else:
            	user=models.User.object.filter(username=username).first()
            if user:
                if user.check_password(password): #校验密码
                    payload = jwt_payload_handler(user) # 把user传入得到payload
                    token = jwt_encode_handler(payload) #把payload传入得到token
                    self.context['token']=token
                    self.context['username']=user.username
                    return attrs
                else:
                    raise ValidationError('密码错误')
			else:
				raise ValidationError('用户不存在') 
```

##### 1.5 jwt的配置参数

```
# jwt的配置
import datetime
JWT_AUTH={
    'JWT_RESPONSE_PAYLOAD_HANDLER':'app02.utils.my_jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7), # 过期时间，手动配置
} 
```

##### 基于角色控制

```
# RBAC :是基于角色的访问控制（Role-Based Access Control ）,公司内部系统
# django的auth就是内置了一套基于RBAC的权限系统
	# 后台的权限控制（公司内部系统，crm，erp，协同平台）
	user表
    permssion表
    group表
    user_groups表是user和group的中间表
    group_permissions表是group和permssion中间表
    user_user_permissions表是user和permission中间表
    # 前台（主站），需要用三大认证
# 演示： 
```

##### django缓存

```
# 前端混合开发缓存的使用
	-缓存的位置，通过配置文件来操作（以文件为例）
    -缓存的粒度：
    	-全站缓存
        	中间件
            MIDDLEWARE = [
                'django.middleware.cache.UpdateCacheMiddleware',
                。。。。
                'django.middleware.cache.FetchFromCacheMiddleware',
            ]
            CACHE_MIDDLEWARE_SECONDS=10  # 全站缓存时间
        -单页面缓存
        	在视图函数上加装饰器
            from django.views.decorators.cache import cache_page
            @cache_page(5)  # 缓存5s钟
            def test_cache(request):
                import time
                ctime=time.time()
                return render(request,'index.html',context={'ctime':ctime})
      
        -页面局部缓存
        	{% load cache %}
            {% cache 5 'name' %}  # 5表示5s钟，name是唯一key值
             {{ ctime }}
            {% endcache %}
      
  
# 前后端分离缓存的使用
	- 如何使用
        from django.core.cache import cache
        cache.set('key',value可以是任意数据类型)
        cache.get('key')
    -应用场景：
    	-第一次查询所有图书，你通过多表联查序列化之后的数据，直接缓存起来
        -后续，直接先去缓存查，如果有直接返回，没有，再去连表查，返回之前再缓存 
```
