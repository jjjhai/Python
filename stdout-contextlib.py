# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:53:03 2018

@author: Administrator
"""

import sys, time, io, contextlib

"""
sys.stdin   标准输入
sys.stdout   标准输出
sys.stderr   标准出错流
"""
j='#'
if __name__ == '__main__':
    for i in range(1,61):
        j += '#'
        #sys.stdout.write(str(int((i/60)*100))+'%  ||'+j+'->'+"\r")
        #sys.stdout.write('#'+'->'+"\b\b")
        #sys.stdout.flush()
        #time.sleep(0.5)
        
 
#等效
print("stdout")
sys.stdout.write("stdout\n")

#sys.stdout重定向
savedStdout = sys.stdout
with open('out.txt', 'w+') as file:
    #sys.stdout = file
    with contextlib.redirect_stdout(file):
        print('This message is for file!')

#标准输出重定向至内存  
#sys.stdout = io.StringIO() 
    
sys.stdout = savedStdout #恢复标准输出流
print('This message is for screen!')


"""
上下文管理器（支持上下文管理协议的对象）
上下文管理协议：包含方法 __enter__() 和 __exit__()
通常使用 with 语句调用上下文管理器
"""

#任何能够被yield关键词分割成两部分的函数，都能够通过装饰器装饰的上下文管理器来实现
#任何在yield之前的内容都可以看做在代码块执行前的操作，而任何yield之后的操作都可以放在exit函数中

#通过装饰生成器函数，省去用__enter__和__exit__写上下文管理器
@contextlib.contextmanager
def redirect_stdout(fileobj):
    
    oldstdout = sys.stdout
    sys.stdout = fileobj
    
    try:
        yield   #需要使用as的时候，yield返回需要的值
    finally:
        sys.stdout = oldstdout



