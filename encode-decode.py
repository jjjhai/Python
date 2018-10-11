# -*- coding: utf-8 -*-
"""
或者 # encoding: utf-8
"""

"""
Created on Wed Mar 14 13:44:56 2018

@author: Administrator
"""


#unicode一般是\u带头的，然后后面跟四位数字或字符串
#utf-8一般是\x带头的，后面跟两位字母或数字，三个\x代表一个汉字
#gbk一般是\x带头的，后面跟两位字母或数字

import sys

print(sys.getdefaultencoding())

#在进行同时包含str类型和unicode类型的字符串操作时，Python2一律都把str解码（decode）成 unicode再运算
#如果函数或类等对象接收的是str类型的字符串，传的是unicode，Python2会默认使用ascii将其编码成str类型再运算
test='测试'
print(type(test))
#repr可以看变量的原始内容
print(repr(test))

#忽略编码错误
#decode('utf-8','ignore')
#encode('utf-8','ignore')
