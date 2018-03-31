# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:08:21 2018

@author: Administrator
"""

l = [1, 2]
print('l之前的id: ', id(l))
l = l + [3, 4]
print('l之后的id: ', id(l))

 
l = [1, 2]
print('l之前的id: ', id(l))
l += [3, 4]
print('l之后的id: ', id(l))

