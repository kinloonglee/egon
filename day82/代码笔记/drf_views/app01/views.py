from django.shortcuts import render

# Create your views here.

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import  APIView

from rest_framework import status
from rest_framework.renderers import JSONRenderer
class TestView(APIView):
    renderer_classes=[JSONRenderer,]
    def get(self,request):
        print(request)

        return Response({'name':'lqz'},status=status.HTTP_200_OK,headers={'token':'xxx'})

class TestView2(APIView):
    def get(self,request):
        print(request)

        return Response({'name':'2222'},status=status.HTTP_200_OK,headers={'token':'xxx'})

##################################视图相关
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

# 基于GenericAPIView写的
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


## 基于GenericAPIView写的Publish的5个接口
from app01.models import Publish
from app01.ser import PublishSerializer
class Publish2View(GenericAPIView):
    #queryset要传queryset对象，查询了所有的图书
    # serializer_class使用哪个序列化类来序列化这堆数据
    queryset=Publish.objects
    # queryset=Book.objects.all()
    serializer_class = PublishSerializer
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


class Publish2DetailView(GenericAPIView):
    queryset = Publish.objects
    serializer_class = PublishSerializer
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

# CURD：create update，delet，retrieve

# 5 个视图扩展类
from rest_framework.mixins import  ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin

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



#GenericAPIView的视图子类 9个
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView

# class Book4View(ListAPIView,CreateAPIView):  #获取所有，新增一个
class Book4View(ListCreateAPIView):  #获取所有，新增一个
    queryset = Book.objects
    serializer_class = BookSerializer

# class Book4DetailView(UpdateAPIView,RetrieveAPIView,DestroyAPIView):
class Book4DetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer



# 使用ModelViewSet编写5个接口
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
class Book5View(ModelViewSet):  #5个接口都有，但是路由有点问题
    queryset = Book.objects
    serializer_class = BookSerializer



class Book5View(ReadOnlyModelViewSet):  #2个接口，获取一条，和获取所有两个
    queryset = Book.objects
    serializer_class = BookSerializer


from rest_framework.viewsets import ViewSetMixin

class Book6View(ViewSetMixin,APIView): #一定要放在APIVIew前


    def get_all_book(self,request):
        print("xxxx")
        book_list = Book.objects.all()
        book_ser = BookSerializer(book_list, many=True)
        return Response(book_ser.data)

