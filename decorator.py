# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:47:29 2018

@author: Administrator
"""
import functools

def short(word="yes"):
    return word.capitalize()+"!"
print(short())

scream = short

del short

try:
    print(short())
except NameError as e:
    print(e)
    
def talk():
    
    def whisper(word="yes"):
        return word.lower()+"..."
    
    print(whisper())

talk()

def decorator(pre=""):
    
    def Fun(F):
        
        def new_Fun(a, b):
            print("new_Fun")
            F(a, b)
            
        return new_Fun
    
    return Fun


@decorator("pre")
def Test(a, b):
    print(a+b)
    
Test(1,2)



"""
多个修饰符时候函数只执行一次，修饰符执行顺序从上到下
"""

def decorator1(f):
    
    def fun():
        print("decorator1")
        f()
    
    return fun


def decorator2(f):
    
    def fun():
        print("decorator2")
        f()
    
    return fun    


@decorator1
@decorator2
def test_decorators():
    print("decorators")

test_decorators()

"""
装饰器内的函数只是代指了原函数，非相等，原函数的元信息没有被赋值到装饰器函数内部
如果使用@functools.wraps装饰装饰器内的函数，那么就会代指元信息和函数。
"""

def outer(func):
   @functools.wraps(func)
   def inner(*args, **kwargs):
       print(inner.__doc__)  # None
       return func()
   return inner
@outer
def test_wraps():
   """
   this is test_wraps description
   """
   print('func')
   


test_wraps()