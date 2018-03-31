# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:50:04 2018

@author: Administrator
"""

from functools import lru_cache

#@functools.lru_cache(maxsize=None, typed=False)
#maxsize为最多缓存的次数，如果为None，则无限制，设置为2n时，性能最佳
#如果typed=True，则不同参数类型的调用将分别缓存，例如 f(3) 和 f(3.0)
@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y

print(add(1, 2))
print(add(1, 2))
print(add(2, 3))