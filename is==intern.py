# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:07:22 2018

@author: Administrator
"""

import copy


"""
is比较的是id值
id()：获取的是对象在内存中的地址
"""

#对象的id值仅仅在对象的生命周期内唯一，在对象被销毁之后, 或被创建之前, 其他对象可以具有相同的id值
class WTF(object):
  def __init__(self): print("I")
  def __del__(self): print("D")

#两个对象创建后再销毁  
print(WTF() is WTF())   #False
#对象创建立即销毁
print(id(WTF()) == id(WTF()))  #True

a = [1, 2, 3]
b = a
print(b is a) #True

print(b == a) #True

b  = a[:]

print(b is a) #False
print(b == a) #True

#Python的缓存 intern机制
c = 1
d = 1
print(c is d) #True
print(1000 is 10**3) #False


# 在Python中-5~256因为被经常使用所以被设计成固定存在的对象
a = 256
b = 256
a is b   # True

a = 257
b = 257
a is b   # False



s = [1,2,3]
#浅拷贝
sc = copy.copy(s)
#深拷贝
sdc = copy.deepcopy(s)
print(sc)
print(sdc)


"""
两者的区别在于拷贝组合对象
比如列表中还有列表，字典中还有字典或者列表的情况时
浅拷贝只拷贝外面的壳子，里面的元素并没有拷贝
而深拷贝则是把壳子和里面的元素都拷贝了一份新的
"""

x = [2, 3]
y = [7, 11]
z = [x, y]

a = copy.copy(z) # 浅拷贝
print(a[0] is z[0])

b = copy.deepcopy(z) # 深拷贝
print(b[0] is z[0])

"""
切片拷贝z[:]属于浅拷贝
自定义__copy__方法和__deepcopy__方法
"""