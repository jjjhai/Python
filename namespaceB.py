# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:48:56 2018

@author: Administrator
"""

"""
标识符：各类对象的名称，比如函数名、方法名、类名，变量名、常量名等
命名空间是存放和使用对象名字的抽象空间
作用域是可以直接访问到命名空间的文本区域
"""

from namespaceA import A

print('b', A)


#global、nonlocal语句说明所修饰的 gv、lv 分别来自全局作用域和父函数作用域
#global语句只是声明该标识符引用的变量来自于全局变量，但并不能直接在当前层创建该标识符
#nonlocal语句则会在子函数命名空间中创建与父函数变量同名的标识符

gv = ['a', 'global', 'var']

def func(v):
    global gv
    gv = ['gv'] + gv
    lv = []
    print(id(lv))
    
    def inn_func():
        nonlocal lv
        lv = lv + [v]
        
        
#类就是一个可执行的代码块，只要该类被加载，就会被执行
#类的局部命名空间并非作用域
class A():
    
    print(1)
    
    class B():
        print(2)
        
        class C():
            print(3)        


