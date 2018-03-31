# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:07:22 2018

@author: Administrator
"""

a = [1, 2, 3]
b = a
print(b is a)

print(b == a)

b  = a[:]

print(b is a)
print(b == a)

#Python的缓存 intern机制
c = 1
d = 1
print(c is d)
print(1000 is 10**3)
