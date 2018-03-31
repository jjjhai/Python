# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:45:28 2018

@author: Administrator
"""

import collections
 
# 初始化字典
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'b' : 3, 'c' : 4 }
 
#ChainMap把map串联到一起
chain = collections.ChainMap(dict1, dict2)
 
# 使用maps输出chainMap
print(chain.maps)  # [{'b': 2, 'a': 1}, {'b': 3, 'c': 4}]
 
# 输出key
print(list(chain.keys()))  # ['b', 'c', 'a']
 
# 输出值
print(list(chain.values())) # [2, 4, 1]
 
# 访问
print(chain['b'])  # 2
print(chain.get('b'))  # 2
 
# 使用new_child添加新字典
dict3 = { 'f' : 5 }
new_chain = chain.new_child(dict3)
print (new_chain.maps)  # [{'f': 5}, {'b': 2, 'a': 1}, {'b': 3, 'c': 4}]

#reversed()函数是返回序列seq的反向访问的迭代子 
new_chain.maps = reversed(new_chain.maps)
print(new_chain.maps)


#命名元祖namedtuple，类似结构体，可以通过 . 访问元组
#多种表达方式，如下
student=collections.namedtuple('student','name age sex')
#student=collections.namedtuple('student',['name','age','sex'])
#student=collections.namedtuple('student','name,age,sex')

spark=student(name='sunYang',age=20,sex='male')
print(spark)
print("spark's name is %s" % spark.name)
print("%s is %d years old %s" % spark)



