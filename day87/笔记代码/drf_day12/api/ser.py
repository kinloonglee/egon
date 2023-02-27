

from rest_framework import serializers
from api import models
from rest_framework.exceptions import ValidationError
class UserModelSerializer(serializers.ModelSerializer):
    re_password=serializers.CharField(max_length=16,min_length=4,required=True,write_only=True) # 因为re_password在表中没有，需要在这定义
    class Meta:
        model=models.User
        fields=['username','password','mobile','re_password','icon']
        extra_kwargs={
            'username':{'max_length':16},
            'password':{'write_only':True}
        }
    # 局部钩子
    def validate_mobile(self,data):
        if not len(data)==11:
            raise ValidationError('手机号不合法')
        return data
    # 全局钩子
    def validate(self, attrs):
        if not attrs.get('password')==attrs.get('re_password'):
            raise ValidationError('两次密码不一致')
        attrs.pop('re_password')# 剔除该字段，因为数据库没有这个字段
        return attrs
    def create(self, validated_data):
        # attrs.pop('re_password') 如果上面没有剔除，在这也可以
        # models.User.objects.create(**validated_data) 这个密码不会加密
        user=models.User.objects.create_user(**validated_data)
        return user


class UserReadOnlyModelSerializer(serializers.ModelSerializer):
   class Meta:
        model=models.User
        fields=['username','icon']

class UserImageModelSerializer(serializers.ModelSerializer):
   class Meta:
        model=models.User
        fields=['icon']
