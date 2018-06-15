# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:00:17 2018

@author: Administrator
"""

#使用模式匹配来搜索文件
import glob
#itertools提供用于操作迭代对象的函数
import itertools as it


#累加
x = it.accumulate(range(10))
print(list(x))   #[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

#连接多个列表或者迭代器
x = it.chain(range(3), range(4), [3,2,1])
print(list(x))   #[0, 1, 2, 0, 1, 2, 3, 3, 2, 1]


#产生指定数目的元素的所有排列(顺序有关)
x = it.permutations(range(4), 3)
print(list(x))


#求列表或生成器中指定数目的元素不重复的所有组合
x = it.combinations(range(4), 3)
print(list(x))   #[(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]


#允许重复元素的组合
x = it.combinations_with_replacement('ABC', 2)
print(list(x))   #[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

#按照真值表筛选元素
x = it.compress(range(5), (True, False, True, True, False))
print(list(x))   #[0, 2, 3]


#对迭代器进行切片
x = it.islice(range(10), 0, 9, 2)
print(list(x))   #[0, 2, 4, 6, 8]

#计数器,可以指定起始位置和步长
x = it.count(start=20, step=-1)
print(list(it.islice(x, 0, 10, 1)))   #[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]


#循环指定的列表和迭代器
x = it.cycle('ABC')
print(list(it.islice(x, 0, 10, 1)))   #['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']

#按照真值函数丢弃掉列表和迭代器前面的元素
x = it.dropwhile(lambda e: e < 5, range(10))
print(list(x))   #[5, 6, 7, 8, 9]

#与dropwhile相反，保留元素直至真值函数值为假。
x = it.takewhile(lambda e: e < 5, range(10))
print(list(x))   #[0, 1, 2, 3, 4]

#保留对应真值为False的元素
x = it.filterfalse(lambda e: e < 5, (1, 5, 3, 6, 9, 4))
print(list(x))   #[5, 6, 9]

#按照分组函数的值对元素进行分组
x = it.groupby(range(10), lambda x: x < 5 or x > 8)                                                                                                
for condition, numbers in x:                                                  
    print(condition, list(numbers))                                                                                                        
#True [0, 1, 2, 3, 4]                                                              
#False [5, 6, 7, 8]                                                                
#True [9]
    

#产生多个列表和迭代器的(积)
x = it.product('ABC', range(3))
print(list(x))   #[('A', 0), ('A', 1), ('A', 2), ('B', 0), ('B', 1), ('B', 2), ('C', 0), ('C', 1), ('C', 2)]


#简单的生成一个拥有指定数目元素的迭代器
x = it.repeat(0, 5)
print(list(x))   #[0, 0, 0, 0, 0]


#类似map
x = it.starmap(str.islower, 'aBCDefGhI')
print(list(x))   #[True, False, False, False, True, True, False, True, False]




#生成指定数目的迭代器
x = it.tee(range(10), 2)
for letters in x:
    print(list(letters))

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#类似于zip，不过已较长的列表和迭代器的长度为准
x = it.zip_longest(range(3), range(5))
y = zip(range(3), range(5))
print(list(x))   #[(0, 0), (1, 1), (2, 2), (None, 3), (None, 4)]
print(list(y))   #[(0, 0), (1, 1), (2, 2)]



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
