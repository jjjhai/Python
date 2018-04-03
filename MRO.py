# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:20:45 2018

@author: Administrator
"""

"""
MRO：方法解析顺序
C3算法：解决单调性问题（经过所有子类再到父类，子类重写的方法只有一种）
        只能继承无法重写问题（经过父类再回子类，最后的子类重写方法无效）
        使用拓扑排序
"""

import inspect

class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

class C(D, F):
    pass

class B(E, D):
    pass

class A(B, C):
    pass

if __name__ == '__main__':
    #查看类的MRO顺序
    print(inspect.getmro(A))
    print(A.__mro__)