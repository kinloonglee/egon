


from rest_framework import serializers
from api import models
import re
from rest_framework.exceptions import ValidationError

from rest_framework_jwt.utils import jwt_encode_handler,jwt_payload_handler
class LoginModelSerializer(serializers.ModelSerializer):
    username=serializers.CharField()  # 重新覆盖username字段，数据中它是unique，post，认为你保存数据，自己有校验没过
    class Meta:
        model=models.User
        fields=['username','password']

    def validate(self, attrs):

        print(self.context)

        # 在这写逻辑
        username=attrs.get('username') # 用户名有三种方式
        password=attrs.get('password')
        # 通过判断，username数据不同，查询字段不一样
        # 正则匹配，如果是手机号
        if re.match('^1[3-9][0-9]{9}$',username):
            user=models.User.objects.filter(mobile=username).first()
        elif re.match('^.+@.+$',username):# 邮箱
            user=models.User.objects.filter(email=username).first()
        else:
            user=models.User.objects.filter(username=username).first()
        if user: # 存在用户
            # 校验密码,因为是密文，要用check_password
            if user.check_password(password):
                # 签发token
                payload = jwt_payload_handler(user)  # 把user传入，得到payload
                token = jwt_encode_handler(payload)  # 把payload传入，得到token
                self.context['token']=token
                self.context['username']=user.username
                return attrs
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')



'''
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

payload = jwt_payload_handler(user) # 把user传入，得到payload
token = jwt_encode_handler(payload) # 把payload传入，得到token

'''