# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:55:37 2018

@author: Administrator
"""
#提供十进制浮点运算支持
import decimal
from decimal import Decimal

#可以传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确
a = decimal.Decimal('0.001')
#默认28位
decimal.getcontext()
d = Decimal(1)/Decimal(9)
print(d)

#改成4位
decimal.getcontext().prec = 4
e = Decimal(1)/Decimal(9)
print(e)

#改成50位
decimal.getcontext().prec =50
f = Decimal(1)/Decimal(9)
print(f)

#不同精度数字可以相加
print(d+e+f)

f = 0.1
#转换为精确的小数表示
print(decimal.Decimal.from_float(f))

#正负无穷大
decimal.Decimal('Infinity')
decimal.Decimal('-Infinity')
  
#不是一个数
decimal.Decimal('NaN')

#取整
#decimal.getcontext().rounding 

#局部上下文
#with decimal.localcontext() as c:
with decimal.localcontext(decimal.Context(prec=50)):
    print(Decimal(355) / Decimal(113))

