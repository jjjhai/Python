# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:38:06 2018

@author: Administrator
"""


va = ['dobi', 'a', 'dog']

print('a1',id(va))

class A():
    def __init__(self):
        pass
    
    def rtn(self):
        global va
        va.insert(1, 'is')
        print('a3', id(va))
        return va

print('a2', va)