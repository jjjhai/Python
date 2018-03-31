# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:52:28 2018
函数式编程
@author: Administrator
"""

from functools import reduce
from functools import partial

def myMap(func, iterable):
    for arg in iterable:
        yield func(arg)
        
names = ["ana", "bob", "dogge"]

print(map(lambda x:x.capitalize(), names))
for name in myMap(lambda x: x.capitalize(), names):
    print(name)
    
def myFilter(func, iterable):
    for arg in iterable:
        if func(arg):
          yield arg

print(filter(lambda x:x % 2 == 0, range(10)))
for i in myFilter(lambda x:x % 2 == 0, range(10)):
    print(i)

print(reduce(lambda a, b: a*b, range(1,5)))

#偏函数
add = lambda a, b: a + b
add1024 = partial(add, 1024)

print(add1024(1))