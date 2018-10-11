# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:18:20 2018

@author: Administrator
"""

import time
from functools import partial
import collections
import threading

import json

import ast

from string import Template

# from module import (xxx, xxx, xxx)

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

"""
实现单例模式方法：
1.使用模块：模块在第一次导入时，会生成.pyc文件
           第二次导入时，会直接加载.pyc文件，而不会再次执行模块代码
           import 对象 from xxx
2.使用__new__：__new__中的类变量cls._instance判断（_instance是类中的字典变量，用于保存所有的实例对象）
3.使用装饰器（decorator）
4.使用元类（metaclass）
5.共享属性：所谓单例就是所有的引用（实例，对象）拥有相同的属性和方法，
           同一个类的实例天生都会有相同的方法，那我们只需要保证同一个类所产生的实例都具有相同的属性
           所有实例共享属性最简单直接的方法就是共享__dict__属性指向
"""



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

#__init__.py文件，一个文件夹中包含这个文件，那么该文件夹在Python中被定义为包


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

# zip:[(1, 'red'),(2, 'green'),(3, 'blue'),(4, 'yellow'),(5, 'black')]，可以通过dict转换为字典
# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便 dict(sape=4139, guido=4127, jack=4098

#有序遍历
#正序
for color in sorted(colors):
    print(color)

#倒序
for color in sorted(colors, reverse=True):
    print(color)


# 转置二维数组
original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)
print(list(transposed))

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

#合并字典
d1 = {'a':1}
d2 = {'b':2}
print({**d1, **d2})  

print(dict(d1.items() | d2.items()))  

d1.update(d2)
print(d1)
    

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

"""
迭代器是一个可以记住遍历位置的对象
迭代器有两个基本的方法：iter() 和 next()
字符串，列表或元组对象都可用于创建迭代器
"""

li = [1, 2, 3]
it = iter(li)
print (next(it))   # 1
for val in it:
    print(val)   # 2 3

        
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



#判断变量num是否为整数类型
num = 1
type(num) == type(0) #调用三次函数
type(num) is type(0) #身份比较
isinstance(num,(int)) #调用一次函数



# 生成器
# (exp for iter_var in iterable)
# 列表解析
# [exp for iter_var in iterable]


# 字符串拼接（连接少量字符串时，推荐使用+号操作符，连接大量字符串时，推荐使用join和f-string方式）
a, b = 'hello', ' world'
# 加号
c=a+b
print(c)

# 逗号（只能用于print打印，赋值操作会生成元组）
print(a,b)

# 直接连接
c = 'hello' ' world'
print(c)

# 使用()多行拼接，python遇到未闭合的小括号，自动将多行拼接为一行
c = ('Hello'
     ' '
     'World'
     '!'
)
print(c)

# 百分号%
c = '%s%s' % (a, b)
print(c)

# format函数
c = '{}{}'.format(a, b)
print(c)

# join函数
c = '-'.join(['aa', 'bb', 'cc'])
print(c)


# f-string
c = f'{a}{b}'
print(c)

# 星号 *
c = a * 3
print(c)

# 通过string模块中的Template对象拼接
c = Template('${s1} ${s2}!')
print(c.safe_substitute(s1='Hello',s2='World'))






# 类型转换
# int(仅支持float、str、bytes)
# float -> int
print(int(-12.94))   # -12

# str -> int
print(int('-12'))   # -12
print(int('+1008'))   # 1008

# bytes -> int
print(int(b'-12'))   # -12

# float(仅支持int、str、bytes)
# int -> float
print(float(-1209))   # -1209.0

# str -> float
print(float('-1209'))   # -1209.0

# bytes -> float
print(float(b'-1209'))   # -1209.0


# complex(仅支持int、float、str)
# int -> complex
print(complex(12))   # (12+0j)

# float -> complex
print(complex(-12.09))   # (-12.09+0j)

# str -> complex
print(complex('-12.09'))   # (-12.09+0j)
print(complex('-12+9j'))   # (-12+9j)
print(complex('(-12+9j)'))   # (-12+9j)
print(complex('-12.0-2.0j'))   # (-12-2j)，去除了小数部分

# str(可以将任意对象转换为字符串)
# float -> str
print(str(-12.90))   # -12.9，去除末位为 0 的小数部分

# complex -> str
print(str(complex(12 + 9j)))   # (12+9j)
print(str(complex(12, 9)))   # (12+9j)

# bytes -> str
print(b'hello world'.decode())   # hello world
print(str(b'hello world', encoding='utf-8'))   # hello world

# list -> str
print(str([1, 2, 3]))   # [1, 2, 3]

# tuple -> str
print((1, 2, 3))   # (1, 2, 3)

# dict -> str
print(str({'name': 'hello', 'age':18}))   # {'name': 'hello', 'age':18}

# set -> str
print(str(set({})))   # set()
print(str({1, 2, 3}))   # {1, 2, 3}

# bytes(仅支持str)
# str -> bytes
print('中国'.encode())   # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(bytes('中国', encoding='utf-8'))   # b'\xe4\xb8\xad\xe5\x9b\xbd'

# list(仅支持序列，比如：str、tuple、dict、set等)
# str -> list
print(list('123abc'))   # ['1', '2', '3', 'a', 'b', 'c']

# bytes -> list（取每个字节的ASCII十进制值并组合成列表）
print(list(b'hello'))   # [104, 101, 108, 108, 111]

# tuple -> list
print(list((1, 2, 3)))   # [1, 2, 3]

# dict -> list（取键名作为列表的值）
print(list({'name': 'hello', 'age': 18}))   # ['name', 'age']

# set -> list（先去重为标准的集合数值，然后再转换）
print(list({1, 2, 3, 3, 2, 1}))   # [1, 2, 3]

# tuple（与list一样）

# dict
# str -> dict
user_info = '{"name": "john", "gender": "male", "age": 28}'
print(json.loads(user_info))

# 使用eval函数
print(eval(user_info))

# 使用ast
user_dict = ast.literal_eval(user_info)
print(user_dict)

# list -> dict
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
print(dict(zip(list1, list2)))   # {1: 1, 2: 2, 3: 3}

li = [
    [1, 111],
    [2, 222],
    [3, 333],
]
print(dict(li))   # {1: 111, 2: 222, 3: 333}

# tuple -> dict
tp1 = (1, 2, 3)
tp2 = (1, 2, 3, 4)
print(dict(zip(tp1, tp2)))   # {1: 1, 2: 2, 3: 3}

tp = (
    (1, 111),
    (2, 222),
    (3, 333),
)
print(dict(tp))   # {1: 111, 2: 222, 3: 333}


# set -> dict
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
print(dict(zip(set1, set2)))   # {1: 'c', 2: 'a', 3: 'b'}

# set
# str -> set
print(set('hello'))   # {'l', 'o', 'e', 'h'}

# bytes -> set（会取每个字节的ASCII十进制值并组合成元组，再去重）
print(set(b'hello'))   # {104, 108, 101, 111}

# list -> set（先对列表去重）
print(set([1, 2, 3, 2, 1]))   # {1, 2, 3}

# tuple -> set（先对列表去重）
print(set((1, 2, 3, 2, 1)))   # {1, 2, 3}

# dict -> set（会取字典的键名组合成集合）
print(set({'name': 'hello', 'age': 18}))   # {'age', 'name'}



# 解包（将容器里面的元素逐个取出来）
# 任何可迭代对象都支持解包，可迭代对象包括元组、字典、集合、字符串、生成器等实现了__next__方法的一切对象
# 字典解包后，只会把字典的key取出来，value则丢掉了
a, b, c = [1,2,3]
a, b, *c = [1,2,3,4]   # c为[3, 4]

#函数调用时的解包操作
def func(a,b,c):
    print(a,b,c)

func(*[1,2,3])
func(*{"a":1,"b":2,"c":3})   # a b c
func(**{"a":1,"b":2,"c":3})   # 1 2 3（**符号作用的对象是字典对象，它会自动解包成关键字参数key=value的格式，但key不是a,b,c时会报错）

# 作用于表达式
*range(4), 4   # (0, 1, 2, 3, 4)
[*range(4), 4]   # [0, 1, 2, 3, 4]
{*range(4), 4}   # {0, 1, 2, 3, 4}
{'x': 1, **{'y': 2}}   # {'x': 1, 'y': 2}

list1 = [1,2,3]
list2 = range(3,6)
[*list1, *list2]



# 多行语句（在[],{},或()中的多行语句，不需要使用反斜杠\）
a = 5 + 3 + \
    2 + 3
print(a)

# 等待用户输入
content = input("请输入点东西并按 Enter 键")
print(content)


# 转义符(\)可以用来转义，使用r可以让反斜杠不发生转义
print(r"this is a line with\n")   # 不换行，输出\n


"""
Python函数的参数传递：
不可变类型：类似c++的值传递，如整数、字符串、元组，如fun(a)，传递的只是a的值，没有影响a对象本身，比如在fun(a)内部修改a的值，只是修改另一个复制的对象，不会影响a本身
可变类型：类似c++的引用传递，如列表、字典，如fun(la)，则是将la真正的传过去，修改后fun外部的la也会受影响
Python中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象
"""

"""
每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行
"""


# 多行表示
my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)
print(my_very_big_string)


"""
any(iterable) -> bool   当iterable所有的值都是0、''、False或者iterable为空，返回False，如果所有元素中有一个值非0、''或False，那么结果就为True
all(iterable) -> bool   当iterable所有元素不为0、''、False或者iterable为空，返回True，否则返回False
"""


