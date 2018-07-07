# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:54:48 2018

@author: Administrator
"""

"""
Python先把代码（.py文件）编译成字节码，交给字节码虚拟机
字节码在Python虚拟机程序里对应的是PyCodeObject对象（.pyc），只有import才会生成.pyc文件，python运行不会

"""

import dis
import sys

#编译得到PyCodeObject对象

"""
使用eval()、exec()函数执行代码时，最好调用代码对象（提前通过compile()函数编译成字节码），而不是直接调用str
正则表达式模式匹配也类似，也最好先将正则表达式模式编译成regex对象（通过re.complie()函数），然后再执行比较和匹配
"""
src = open('pycodeobject-test.py', encoding='utf-8').read()
#将一个字符串编译为字节代码，exec对应Python语句，eval对应Python表达式
co = compile(src, 'pycodeobject.py', 'exec')
#print(dir(co))

#所有符号名称集合
#print(co.co_names)

#所有常量集合 
#print(co.co_consts)

#字节码指令序列
#print(co.co_code)

#解析指令序列
print(dis.dis(co.co_consts[2]))
"""
第一列表示以下几个指令在py文件中的行号
第二列是该指令在指令序列co_code里的偏移量
第三列是指令opcode的名称，分为有操作数和无操作数两种，opcode在指令序列中是一个字节的整数
第四列是操作数oparg，在指令序列中占两个字节，基本都是co_consts或者co_names的下标
第五列带括号的是操作数说明
 11           0 LOAD_GLOBAL              0 (print) 全局变量压栈
              2 LOAD_GLOBAL              1 (s)
              4 CALL_FUNCTION            1  调用函数，创建新的栈帧并在新栈帧上执行
              6 POP_TOP                     函数返回值出栈
              8 LOAD_CONST               0 (None) None压栈
             10 RETURN_VALUE
"""

"""
获取当前栈帧
frame = sys._getframe()
print(frame.f_locals) 本地名字空间
print(frame.f_globals) 全局名字空间
print(frame.f_back.f_locals) 调用者的帧的本地名字空间
"""

