from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from api import models
from  rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from api.ser import BookModelSerializer

class BookAPIView(APIView):
    def get(self,request,*args,**kwargs):
        #查询单个和查询所有，合到一起
        # 查所有
        book_list=models.Book.objects.all().filter(is_delete=False)
        book_list_ser=BookModelSerializer(book_list,many=True)
        return Response(data=book_list_ser.data)
        #查一个

    def post(self,request,*args,**kwargs):
        # 具备增单条，和增多条的功能
        if isinstance(request.data,dict):

            book_ser=BookModelSerializer(data=request.data)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
        elif isinstance(request.data,list):
            #现在book_ser是ListSerializer对象
            from rest_framework.serializers import ListSerializer
            book_ser = BookModelSerializer(data=request.data,many=True)  #增多条
            print('--------',type(book_ser))
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            # 新增---》ListSerializer--》create方法
            # def create(self, validated_data):
            #   self.child是BookModelSerializer对象
            #   print(type(self.child))
            #     return [
            #         self.child.create(attrs) for attrs in validated_data
            #     ]
            return Response(data=book_ser.data)

    def put(self,request,*args,**kwargs):
        # 改一个，改多个
        #改一个个
        if kwargs.get('pk',None):
            book=models.Book.objects.filter(pk=kwargs.get('pk')).first()
            book_ser = BookModelSerializer(instance=book,data=request.data,partial=True)  # 增多条
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
        else:
            #改多个,
            # 前端传递数据格式[{id:1,name:xx,price:xx},{id:1,name:xx,price:xx}]
            # 处理传入的数据  对象列表[book1，book2]  修改的数据列表[{name:xx,price:xx},{name:xx,price:xx}]
            book_list=[]
            modify_data=[]
            for item in request.data:
                #{id:1,name:xx,price:xx}

                pk=item.pop('id')
                book=models.Book.objects.get(pk=pk)
                book_list.append(book)
                modify_data.append(item)
            # 第一种方案，for循环一个一个修改
            #把这个实现
            # for i,si_data in enumerate(modify_data):
            #     book_ser = BookModelSerializer(instance=book_list[i], data=si_data)
            #     book_ser.is_valid(raise_exception=True)
            #     book_ser.save()
            # return Response(data='成功')
            # 第二种方案，重写ListSerializer的update方法
            book_ser = BookModelSerializer(instance=book_list,data=modify_data,many=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()  #ListSerializer的update方法,自己写的update方法
            return Response(book_ser.data)
            # request.data
            #
            # book_ser=BookModelSerializer(data=request.data)

    def delete(self,request,*args,**kwargs):
        #单个删除和批量删除
        pk=kwargs.get('pk')
        pks=[]
        if pk:
            # 单条删除
            pks.append(pk)
        #不管单条删除还是多条删除，都用多条删除
        #多条删除
        # {'pks':[1,2,3]}
        else:
            pks=request.data.get('pks')
        #把is_delete设置成true
        # ret返回受影响的行数
        ret=models.Book.objects.filter(pk__in=pks,is_delete=False).update(is_delete=True)
        if ret:
            return Response(data={'msg':'删除成功'})
        else:
            return Response(data={'msg': '没有要删除的数据'})







# 查所有，才需要分页
from rest_framework.generics import ListAPIView
# 内置三种分页方式
from  rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
'''
PageNumberPagination
    page_size:每页显示的条数
'''
class MyPageNumberPagination(PageNumberPagination):
    #http://127.0.0.1:8000/api/books2/?aaa=1&size=6
    page_size=3  #每页条数
    page_query_param='aaa' #查询第几页的key
    page_size_query_param='size' # 每一页显示的条数
    max_page_size=5    # 每页最大显示条数


# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 3   # 每页条数
#     limit_query_param = 'limit' # 往后拿几条
#     offset_query_param = 'offset' # 标杆
#     max_limit = 5   # 每页最大几条

class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'  # 每一页查询的key
    page_size = 2   #每页显示的条数
    ordering = '-id'  #排序字段
# class BookView(ListAPIView):
#     # queryset = models.Book.objects.all().filter(is_delete=False)
#     queryset = models.Book.objects.all()
#     serializer_class = BookModelSerializer
#     #配置分页
#     pagination_class = MyCursorPagination

# 如果使用APIView分页
from utils.throttling import MyThrottle
class BookView(APIView):
    # throttle_classes = [MyThrottle,]
    def get(self,request,*args,**kwargs):
        book_list=models.Book.objects.all()
        # 实例化得到一个分页器对象
        page_cursor=MyPageNumberPagination()

        book_list=page_cursor.paginate_queryset(book_list,request,view=self)
        next_url =page_cursor.get_next_link()
        pr_url=page_cursor.get_previous_link()
        # print(next_url)
        # print(pr_url)
        book_ser=BookModelSerializer(book_list,many=True)
        return Response(data=book_ser.data)

