# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:07:22 2018

@author: Administrator
"""

"""
参数：
value: 打印的值，可多个
file: 输出流，默认是 sys.stdout
sep: 多个值之间的分隔符
end: 结束符，默认是换行符 
flush: 是否强制刷新到输出流，默认否
"""

# 分隔符（默认是空格）
print(1, 2, 3, sep='-')

# 结束符
print('第一行', end='-')

print('第二行')

# 输出重定向
with open('data.log', 'w') as fileObj:
    print('hello world!', file=fileObj)