# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:40:48 2018

@author: Administrator
"""

import pickle
import json

 
variable = ['hello', 42, [1,'two'],'apple']

file = open('serial.txt','wb')
#序列化
serialized_obj = pickle.dumps(variable)
file.write(serialized_obj)
file.close()

 
target = open('serial.txt','rb')
#反序列化
myObj = pickle.load(target)

print(serialized_obj)
print(myObj)



print("Original {0} - {1}".format(variable,type(variable)))

#encoding
encode = json.dumps(variable)
print("Encoded {0} - {1}".format(encode,type(encode)))

#deccoding
decoded = json.loads(encode)
print("Decoded {0} - {1}".format(decoded,type(decoded)))