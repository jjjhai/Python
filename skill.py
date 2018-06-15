# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:18:20 2018

@author: Administrator
"""

import time
from functools import partial
import collections
import threading

def fun():
    print('fun')

def fun1():
    print('fun1')

#发布package时可以import的类或者函数名    
__all__ = ['fun']

#with语句需要支持上下文管理协议的对象
#上下文管理协议包含 __enter__ 和 __exit__ 两个方法
#open("datetime.py", "r")是上下文表达式
with open("datetime.py", "r") as my_file: #__enter__()方法的返回值赋值给my_file
    print("open")
    
    
lst = [1, 2, 3]
#lst = None
new_lst = lst[0] if lst is not None else None
print(new_lst)

# 单例装饰器

def singleton(cls):
    
    instances = dict()  # 初始为空
    
    def _singleton(*args, **kwargs):
        if cls not in instances:  #如果不存在, 则创建并放入字典
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return _singleton

#eval:解释字符串为对应的代码并执行
#exec会忽略返回值
def test_first():
    return 3

def test_second(num):
    return num

action = {  # 可以看做是一个sandbox
        "para": 5,
        "test_first" : test_first,
        "test_second": test_second
}

def test_eavl():  
    condition = "para == 5"
    res = eval(condition, action)  # 解释condition并根据action对应的动作执行
    print(res)
    
test_eavl()

#通过string类型的name，返回对象的name属性(方法)对应的值
#getattr(对象, name)


#默认参数在定义的时候求值
def report(when=None):
    if when is None:
        when = time.time()
        
    return when

print(report())
print(report())

#生成一个元素是列表的列表x
b = [[]] * 10
a = [[] for _ in range(10)]
a[0].append(10)
print(a)

def create_multipliers():
    return [lambda x, i = i:i*x for i in range(5)]

print(create_multipliers())
for multiplier in create_multipliers():
    print(multiplier(2))
    
#一行代码交换两个变量值
c=8
d=9
(c,d) = (d,c)
#c,d = d,c
print(c, d)

#__init__.py文件


#浮点数
#无限大
print(float('infinity'))


#遍历元素和索引
bag = [1, 2, 3, 4, 5]
for index, element in enumerate(bag):  
    print(index, element)

#反向遍历
for e in reversed(bag):
    print(e)

colors = ['red', 'green', 'blue', 'yellow', 'black'] 
#遍历两个集合
for ba, color in zip(bag, colors):
    print(ba, '--->', color)

#有序遍历
#正序
for color in sorted(colors):
    print(color)

#倒序
for color in sorted(colors, reverse=True):
    print(color)


#函数有多个返回值
def binary():
    return 0, 1

zero, one = binary()
#_返回所有值 
zero, _ = binary()

countr = {}  

#访问字典
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
#countr = dict([(num, bag.count(num)) for num in bag])   #开销大
#countr = {num: bag.count(num) for num in bag}   #开销大
for i in bag:  
    countr[i] = countr.get(i, 0) + 1
    #countr[i] = countr.setdefault(i, 0) + 1

for i in range(10):  
    print("Count of {}: {}".format(i, countr.get(i, 0)))
    


#在访问的时候操作字典
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in list(d.keys()):
    if k.startswith('r'):
        del d[k]
#遍历字典
for k, v in d.items():
    print(k, '--->', v)        
 
#popitem是原子的
while d:
    key, value = d.popitem()
    print(key, '-->', value)


      
#链式比较操作
age = 20
if 18 < age < 60:
    print("yong man")
    
print(False == False == True)

#if/else 三目运算
gender = 'male'
text = '男' if gender == 'male' else '女' 

#容器没有元素的时候返回False
values = []
if values:
    print('no empty')

#for/else语句
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    print(i)
else:
    #在for循环遍历完所有元素之后执行
    print('finish')


#调用一个函数直到遇到标记值
#blocks = []
#iter函数把列表对象转化为迭代器对象
#iter接受两个参数。第一个是你反复调用的函数，第二个是标记值
#for block in iter(partial(f.read, 32), ''):
    #blocks.append(block)   
    

#unpack序列
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'
fname, lname, age, email = p
print(fname)

#连接字符串
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
print(', '.join(names))

#更新序列
name2s = collections.deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])
name2s.popleft()
name2s.appendleft('mark')
print(name2s)


# 使用锁的新方法
lock = threading.Lock()
with lock:
    print('Critical section 1')
    print('Critical section 2')
    

#程序中小数点的二进制表示
#将该数字小数部分乘以2，取出整数部分作为二进制表示的第1位
#然后再将小数部分乘以2，将得到的整数部分作为二进制表示的第2位
#以此类推，直到小数部分为0


#提高可读性    
number = 100_00_00
print(number)


a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.') #'Five plus ten is 15 and not 30.'

# 精度
PI = 3.141592653
print(f"Pi is {PI:.2f}") #'Pi is 3.14'

error = 50159747054
#以16进制格式化
print(f'Programmer Error: {error:#x}') #'Programmer Error: 0xbadc0ffee'

#以二进制格式化
print(f'Programmer Error: {error:#b}') #'Programmer Error: 0b101110101101110000001111111111101110'

    
def my_add(a: int, b: int) -> int:
    return a + b

