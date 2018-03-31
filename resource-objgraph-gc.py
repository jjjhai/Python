# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:30:27 2018

@author: Administrator
"""
"""
导致引用计数+1的情况
1.对象被创建，例如a=23
2.对象被引用，例如b=a
3.对象被作为参数，传入到一个函数中，例如func(a)
4.对象作为一个元素，存储在容器中，例如list1=[a,a]

导致引用计数-1的情况
1.对象的别名被显式销毁，例如del a
2.对象的别名被赋予新的对象，例如a=24
3.一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
4.对象所在的容器被销毁，或从容器中删除对象
"""

#import Resource
import objgraph
import random
import sys
import gc

#print(Resource.getrusage(Resource.RUSAGE_SELF).ru_maxrss)

class Foo(object):
    #减少内存消耗小技巧
    __slots__ = ('val',)
    
    def __init__(self):
        self.val = None
    
    def __str__(self):
        return "foo - val：{ 0 }".format(self.val)
    
    def __del__(self):
        print('Object del')
    
def f():
    l = []
    for i in range(3):
        foo = Foo()
        l.append(foo)
    return l

def main():
    d = {}
    l = f()
    d['k'] = l
    
    print("list l has {0} objects of type Foo()".format(len(l)))
    
    objgraph.show_most_common_types()
    #objgraph.show_backrefs(random.choice(objgraph.by_type('Foo')),filename="foo_refs.png")
    #objgraph.show_refs(d, filename='sample-graph.png')

if __name__ == "__main__":
    main()
    

t = "abcdefghijklmnopqrstuvwxyz"
p = "abcdefghijklmnopqrstuvwxyz"
print(hex(id(t)))
print(id(p))

a=b=c=d='gg'
#减少内存消耗小技巧:使用Format来代替“+”构建字符串。
st = "{0}_{1}_{2}_{3}".format(a,b,c,d)   # 对内存更好，不创建临时变量st
st2 = a + '_' + b + '_' + c + '_' + d # 在每个"+"时创建一个临时str，这些都是驻留在内存中的。

print(st)


print("init", sys.getrefcount(11)-1)

#垃圾回收
#设置gc的debug日志，一般设置为gc.DEBUG_LEAK
gc.set_debug(gc.DEBUG_LEAK)
#触发垃圾回收,返回不可达对象数目
#分代收集的方法，把对象分为三代，对象在创建的时候，放在一代中，如果在一次一代的垃圾检查中，对象存活下来，就会被放到二代中
gc.collect()
#设置自动执行垃圾回收的频率
#gc.set_threshold()
#自动垃圾回收的阀值
print(gc.get_threshold())

#如果循环引用中，两个对象都定义了__del__方法，gc模块不会销毁这些不可达对象
#因为gc模块不知道应该先调用哪个对象的__del__方法，所以为了安全起见，gc模块会把对象放到gc.garbage中，但是不会销毁对象
print(gc.garbage)

#获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表
print(gc.get_count())

    

#fgc()
