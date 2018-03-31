# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:53:16 2018

@author: Administrator
"""

"""
descr.__get__(self, obj, objtype=None) --> value
descr.__set__(self, obj, value) --> None
descr.__delete__(self, obj) --> None
只要一个object attribute(对象属性)定义了上面三个方法中的任意一个，那么这个类就可以被称为描述符类
"""



#描述符类
class RevealAccess(object):
    #obj是调用的对象（m）,objtype是调用的对象类型
    def __get__(self, obj, objtype):
        print('self in RevealAccess: {}'.format(self))
        print('self: {}\nobj: {}\nobjtype: {}'.format(self, obj, objtype))
        
class MyClass(object):
    x = RevealAccess()
    
    def test(self):
        print('self in MyClass: {}'.format(self))
        
m = MyClass()
m.test()
#调用object.__getattribute__()转译成type(m).__dict__['x'].__get__(m, type(m))
m.x
#调用type.__getattribute__()转译成MyClass.__dict__['x'].__get__(None, MyClass)
MyClass.x


#数据描述符（data descriptor）：一个对象同时定义了__get__()和__set__()方法
#非数据描述符（non-data descriptor）：一个对象只定义了__get__()方法

#优先级：数据描述符＞实体属性（存储在实体的_dict_中）>非数据描述符 > __getattr__()
#首先，看这个属性是不是一个数据描述符，如果是，就直接执行描述符的__get__，并返回值
#其次，如果这个属性不是数据描述符，那就按常规去从__dict__里面取(是否在类中有定义)
#最后，如果__dict__里面还没有，但这是一个非数据描述符，则执行非数据描述符的__get__方法，并返回 
#__getattribute__优先级是最高的, 而__getattr__是最低的

#静态字段方式
class Account(object):
    def __init__(self):
        self._acct_num = None
    
    def get_acct_num(self):
        print("get_acct_num")
        return self._acct_num
    
    def set_acct_num(self, value):
        print("set_acct_num")
        self._acct_num = value
    
    def del_acct_num(self):
        print("del_acct_num")
        del self._acct_num
        
    acct_num = property(get_acct_num, set_acct_num, del_acct_num, '_acct_num property.')

#acc = Account()
#acc.acct_num = 100

#装饰器方式
class AccountI(object):
    
    def __init__(self, acct_num):
        self._acct_num = acct_num
    
    @property
    def acct_num(self):
        print("get_acct_num I")
        return self._acct_num 
    
    @acct_num.setter
    def set_acct_num(self, value):
        print("set_acct_num I")
        self._acct_num = value
    
    @acct_num.deleter
    def del_acct_num(self):
        print("del_acct_num I")
        del self._acct_num
    


acc = AccountI(100)
#acc.acct_num = 200
print(acc.acct_num)


#使用非数据描述符模拟静态方法的实现
class StaticMethod(object):
    def __init__(self, f):
        self.f = f
        
    def __get__(self, obj, objtype=None):
        return self.f

class MyClass(object):
    
    @StaticMethod
    def get_x(x):
        return x
    
print(MyClass.get_x(10))


#使用非数据描述符来模拟类方法的实现：
class ClassMethod(object):
    def __init__(self, f):
        self.f = f
        
    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
            
        def newfunc(*args):
            return self.f(klass, *args)

        return newfunc





