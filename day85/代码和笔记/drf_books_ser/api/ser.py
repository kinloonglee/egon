

from rest_framework import serializers
from api import models


#写一个类，继ListSerializer,重写update
class BookListSerializer(serializers.ListSerializer):
    # def create(self, validated_data):
    #     print(validated_data)
    #     return super().create(validated_data)
    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        # 保存数据
        # self.child:是BookModelSerializer对象
        # ll=[]
        # for i,si_data in enumerate(validated_data):
        #     ret=self.child.update(instance[i],si_data)
        #     ll.append(ret)
        # return ll
        return [
            # self.child.update(对象，字典) for attrs in validated_data
            self.child.update(instance[i],attrs) for i,attrs in enumerate(validated_data)
        ]



#如果序列化的是数据库的表，尽量用ModelSerializer
class BookModelSerializer(serializers.ModelSerializer):
    # 一种方案（只序列化可以，反序列化有问题）
    # publish=serializers.CharField(source='publish.name')
    # 第二种方案，models中写方法

    class Meta:
        list_serializer_class=BookListSerializer
        model=models.Book
        # fields='__all__'
        # 用的少
        # depth=0
        sss=serializers.CharField(source='name')
        fields = ('id','name','price','authors','publish','publish_name','author_list','ssss')

        extra_kwargs={
            'publish':{'write_only':True},
            'publish_name':{'read_only':True},
            'authors':{'write_only':True},
            'author_list':{'read_only':True}
        }