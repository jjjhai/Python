# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:40:48 2018

@author: Administrator
"""

import pickle
import json

 
variable = ['hello', 42, [1,'two'],'apple']

file = open('serial.txt','wb')

# 将数据对象序列化后写入文件
# pickle.dump(variable, file)

#序列化
#以字节对象形式返回封装的对象，不需要写入文件中
serialized_obj = pickle.dumps(variable)
file.write(serialized_obj)
file.close()

 
target = open('serial.txt','rb')
#反序列化
# 从文件中读取内容并反序列化
myObj = pickle.load(target)

# 从字节对象中读取被封装的对象，并返回
# pickle.loads

print(serialized_obj)
print(myObj)



print("Original {0} - {1}".format(variable,type(variable)))

#encoding
#encode = json.dumps(variable, indent=2) 格式化json数据
encode = json.dumps(variable)
print("Encoded {0} - {1}".format(encode,type(encode)))

#deccoding
decoded = json.loads(encode)
print("Decoded {0} - {1}".format(decoded,type(decoded)))