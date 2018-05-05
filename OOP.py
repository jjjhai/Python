# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:22:25 2018

@author: Administrator
"""

"""
当前类或者父类继承了object类，那么该类便是新式类，否则便是经典类
当类是经典类时，多继承情况下，会按照深度优先方式查找
当类是新式类时，多继承情况下，会按照广度优先方式查找
"""

class Animals(object):
    def __init__(self):
        print("Animals")

class Animal(object):
    
    def __init__(self):
        print("Animal")
        
    def eat(self):
        print("%s 吃 " % self.name)
        
    def drink(self):
        print("%s 喝 " % self.name)

    def shit(self):
        print("%s 拉 " % self.name)
        
    def pee(self):
        print("%s 撒 " % self.name)

 
class Cat(Animal, Animals):
    
    def __init__(self, name):
        super(Cat, self).__init__()   #输出Animal
        self.name = name
        self.breed = '喵'
    
    def cry(self):
        print('喵喵叫')

 
class Dog(Animals, Animal):
    
    def __init__(self, name):
        #Animals.__init__(self)
        super(Dog, self).__init__()   #输出Animals
        self.name = name
        self.breed = '汪'

    def cry(self):
        print('汪汪叫')

cat = Cat('小猫')
dog = Dog('小狗')        
        

"""
类成员包括普通字段、静态字段、普通方法、类方法、静态方法、普通属性
类创建多少对象，在内存中就有多少个普通字段，而其他成员，则都是保存在类中
普通字段属于对象，静态字段属于类
"""

"""·
公有静态字段：类可以访问、类内部可以访问、派生类中可以访问
私有静态字段：仅类内部可以访问

公有普通字段：对象可以访问、类内部可以访问、派生类中可以访问
私有普通字段：仅类内部可以访问

强制访问私有字段：对象._类名__私有字段名

__为私有，_为保护
"""
class Province:
    
    #静态字段
    country = '中国'
    
    sta_pub = '共有静态字段'
    __sta_pro = '私有静态字段'
    
    
    def __init__(self, name):
        #普通字段
        self.name = name
        self.__foo = '私有普通字段'
    
    def ord_func(self):
        print('普通方法')
    
    @classmethod
    def class_func(cls):
        print('类方法')
    
    @staticmethod    
    def static_func():
        print('静态方法')
 
#直接访问普通字段
obj = Province('河北省')
print(obj.name)

#直接访问静态字段
print(Province.country)

obj.ord_func()
Province.class_func()
Province.static_func()
obj.static_func()


"""
类的特殊成员：
"""


class Foo(object):
    
    """ 描述类信息，这是用于看片的神奇 """
    
    def __init__(self, sq):
        self.sq = sq
    
    #迭代    
    def __iter__(self):
        return iter(self.sq)
    
    def func(self):
        pass
    
    def __call__(self, *args, **kwargs):
        print('类实例当做函数调用')
        
    def __str__(self):
        return 'str'
    
    def __getitem__(self, key):
        print('__getitem__',key)
    
    def __setitem__(self, key, value):
        print('__setitem__',key,value)
        
    def __delitem__(self, key):
        print('__delitem__',key)    
    

foo = Foo([11,22,33,44])
 
#类的描述信息
print(Foo.__doc__)
#表示当前操作的对象在哪个模块
print(foo.__module__)
#表示当前操作的对象的类是什么
print(foo.__class__)
#类的所有父类构成元素（包含了一个由所有父类组成的元组）
print(Foo.__bases__) 
#__call__对象后面加括号，触发执行
foo()
#获取类的成员
print(Foo.__dict__)
#获取对象的成员
print(foo.__dict__)
#调用__str__方法
print(foo)
#__repr__和__str__这两个方法都是用于显示，__str__是面向用户的(print)，而__repr__面向程序员(交互式直接打印)
#str内置函数和repr内置函数直接调用

"""
运算符重载：
__add__：+
__mul__：*

"""

"""
__getitem__、__setitem__、__delitem__
用于索引操作，如字典。以上分别表示获取、设置、删除数据
"""
#result = foo['k1']      #自动触发执行__getitem__
#foo['k2'] = 'wupeiqi'   #自动触发执行__setitem__
#del foo['k1']           #自动触发执行__delitem__

foo[-1:1]                   #自动触发执行__getitem__
foo[0:1] = [11,22,33,44]    #自动触发执行__setitem__
del foo[0:2]                #自动触发执行__delitem__

for i in foo:
    print(i)

"""    
特殊方法创建类,类是由type类实例化产生
"""
print(type(Foo))
def func(self):
    print('hello wupeiqi')
#第二个参数为基类
Foos = type('Foos',(object,), {'func': func})


#__new__ 和 __metaclass__
#__metaclass__用来表示该类由谁来实例化创建
class MyType(type):
    
    #创建Fooes的时候调用
    def __init__(self, what, bases=None, dict=None):
        super(MyType, self).__init__(what, bases, dict)
    
    #Fooes()的时候调用    
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj)

class Fooes(object):
    
    __metaclass__ = MyType
    
    def __init__(self):
        self.name = None
         
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Fooes()