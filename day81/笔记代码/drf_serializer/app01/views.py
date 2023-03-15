from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer
from app01.ser import BookModelSerializer
from rest_framework.response import Response  #drf 提供的响应对象

# 导入自己写的response类
from app01.utils import MyResponse
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

    def delete(self,request,pk):
        response=MyResponse()
        ret=Book.objects.filter(pk=pk).delete()
        return Response(response.get_dict)

class BooksView(APIView):
    # def get(self,request):
    #     response_msg = {'status': 100, 'msg': '成功'}
    #     books=Book.objects.all()
    #     book_ser=BookSerializer(books,many=True)  #序列化多条,如果序列化一条，不需要写
    #     response_msg['data']=book_ser.data
    #     return Response(response_msg)

    def get(self,request):
        response=MyResponse()
        books=Book.objects.all()
        book_ser=BookSerializer(books,many=True)  #序列化多条,如果序列化一条，不需要写
        response.data=book_ser.data
        return Response(response.get_dict)

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


class BooksView2(APIView):
    def get(self,request):
        response=MyResponse()
        books=Book.objects.all()
        book=Book.objects.all().first()
        book_ser=BookModelSerializer(books,many=True)
        book_one_ser=BookModelSerializer(book)
        print(type(book_ser))
        print(type(book_one_ser))
        response.data=book_ser.data
        return Response(response.get_dict)

