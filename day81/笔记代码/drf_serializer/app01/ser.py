
# from rest_framework.serializers import Serializer  # 就是一个类
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
# 需要继承 Serializer
from app01.models import Book

def check_author(data):
    if data.startswith('sb'):
        raise ValidationError('作者名字不能以sb开头')
    else:
        return data


class BookSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField(max_length=16,min_length=4)
    # price=serializers.DecimalField()
    price=serializers.CharField(write_only=True,required=True)
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
    def create(self, validated_data):
        instance=Book.objects.create(**validated_data)
        return instance
        # Book.objects.create(name=validated_data.get('name'))


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

