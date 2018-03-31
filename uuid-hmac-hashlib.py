# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:15:05 2018

@author: Administrator
"""

import uuid
import hmac,hashlib

#生成唯一ID
result = uuid.uuid1()
print(result)

#python可用的加密函数
print(hashlib.algorithms_available)

#python在所有平台上都可以使用的函数，也就是比较稳定的函数
print(hashlib.algorithms_guaranteed)

#创建一个加密函数对象
m = hashlib.md5()
m.update('python isinteresting'.encode('utf-8'))
print(m.hexdigest())

myhmac = hmac.new(b'mykey')
myhmac.update(b'mymessage')
print(myhmac.hexdigest())

key=b'1'
data=b'a'
print(hmac.new(key, data, hashlib.sha256).hexdigest())

 