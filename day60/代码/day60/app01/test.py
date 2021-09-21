import json

import  requests
import json

ip_str=requests.get("http://httpbin.org/ip").text
print(ip_str,type(ip_str))
ip=json.loads(ip_str).get("origin")
print(ip)