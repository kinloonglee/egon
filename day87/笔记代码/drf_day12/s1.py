

# base64编码和解码
#md5固定长度，不可反解
#base63 变长，可反解

#编码（字符串，json格式字符串）
import base64
import json
dic={'name':'lqz','age':18,'sex':'男'}
dic_str=json.dumps(dic)

ret=base64.b64encode(dic_str.encode('utf-8'))
print(ret)

# 解码
# ret是带解码的串
ret2=base64.b64decode(ret)
print(ret2)
