# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:35:39 2018

@author: Administrator
"""

"""
闭包各自独立拥有一块封闭起来的作用域，不受全局变量或者任何其它运行环境的影响
"""

def inc():
    x = 0
    def inner():
        nonlocal x
        x += 1
        print(x)
    return inner

inc1 = inc()
inc2 = inc()

inc1()
inc1()
inc1()
inc2()

#闭包函数都有一个__closure__属性，其中包含了它所引用的上层作用域中的变量：
print(inc1.__closure__[0].cell_contents)
print(inc2.__closure__[0].cell_contents)
