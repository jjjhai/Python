# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 14:23:17 2018

@author: Administrator
"""

"""
模式   可做操作	若文件不存在	是否覆盖
r	    只能读	      报错	          -
r+	   可读可写	   报错	          是
w	    只能写	       创建	       是
w+　	可读可写	   创建           是
a　　	 只能写	       创建	    否，追加写
a+	   可读可写	   创建	       否，追加写

"""

"""
fileObject.flush()
flush()方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入
一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用flush()方法

fileObject.fileno()
fileno()方法返回一个整型的文件描述符(file descriptor FD整型)，可用于底层操作系统的I/O操作

fileObject.isatty()
isatty()方法检测文件是否连接到一个终端设备，如果是返回True，否则返回False

next(iterator[,default])
Python3中的File对象不支持next()方法。 Python3的内置函数next()通过迭代器调用__next__()方法返回下一项
在循环中，next()函数会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF)，则触发StopIteration

fileObject.read()
read()方法用于从文件读取指定的字节数，如果未给定或为负则读取所有

fileObject.readline()
readline()方法用于从文件读取整行，包括 “ ” 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 “ ” 字符

fileObject.readlines()
readlines()方法用于读取所有行(直到结束符EOF)并返回列表，该列表可以由Python的for... in ... 结构进行处理。如果碰到结束符 EOF，则返回空字符串。

fileObject.seek(offset[, whence])
seek()方法用于移动文件读取指针到指定位置。
whence的值, 如果是0表示开头, 如果是1表示当前位置, 2表示文件的结尾。whence 值为默认为0，即文件开头。例如：
seek(x, 0)：从起始位置即文件首行首字符开始移动x个字符
seek(x, 1)：表示从当前位置往后移动x个字符
seek(-x, 2)：表示从文件的结尾往前移动x个字符

fileObject.tell(offset[, whence])
tell()方法返回文件的当前位置，即文件指针当前位置

fileObject.truncate([size])
truncate()方法用于从文件的首行首字符开始截断，截断文件为size个字符，无size表示从当前位置截断
截断之后V后面的所有字符被删除，其中Widnows系统下的换行代表2个字符大小

fileObject.write([str])
write()方法用于向文件中写入指定字符串
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的
如果文件打开模式带b，那写入文件内容时，str(参数)要用encode方法转为bytes形式，否则报错：TypeError: a bytes-like object is required, not 'str'

fileObject.writelines([str])
writelines()方法用于向文件中写入一序列的字符串。这一序列字符串可以是由迭代对象产生的，如一个字符串列表。换行需要指定换行符
"""



filename = 'data.log'
# 打开文件(a+ 追加读写模式)
# 用 with 关键字的方式打开文件，会自动关闭文件资源
with open(filename, 'w+', encoding='utf-8') as file:
    print('文件名称: {}'.format(file.name))
    print('文件编码: {}'.format(file.encoding))
    print('文件打开模式: {}'.format(file.mode))
    print('文件是否可读: {}'.format(file.readable()))
    print('文件是否可写: {}'.format(file.writable()))
    print('此时文件指针位置为: {}'.format(file.tell()))
    # 写入内容
    num = file.write("第一行内容")
    print('写入文件{}个字符'.format(num))
    # 文件指针在文件尾部，故无内容
    print(file.readline(), file.tell())
    # 改变文件指针到文件头部
    file.seek(0)
    # 改变文件指针后，读取到第一行内容(文件指针回到了文件尾，tell返回15)
    print(file.readline(), file.tell())
    # 在文件尾写入
    file.write('第二次写入的内容')
    # 文件指针又回到了文件尾
    print(file.readline(), file.tell())
    # file.read() 从当前文件指针位置读取指定长度的字符
    file.seek(0)
    print(file.read(9))
    # 按行分割文件，返回字符串列表
    file.seek(0)
    print(file.readlines())
    # 迭代文件对象，一行一个元素
    file.seek(0)
    for line in file:
        print(line, end='')
        
# 关闭文件资源
if not file.closed:
    file.close()