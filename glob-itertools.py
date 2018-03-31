# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:00:17 2018

@author: Administrator
"""

#使用模式匹配来搜索文件
import glob
#itertools提供用于操作迭代对象的函数
import itertools as it

#count()创建一个无限的迭代器
#cycle()把传入的一个序列无限重复下去
#repeat()把一个元素重复下去
#chain()把一组迭代对象串联起来
#groupby()把迭代器中相邻的重复元素挑出来放在一起
#imap()可以作用于无穷序列
#ifilter()是filter()的惰性实现
def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.glob(pattern) for pattern in patterns)

 
for filename in multiple_file_types("*.txt", "*.py"): # add as many filetype arguements
    print(filename)

#files = glob.glob('*.py')
#print(files)
