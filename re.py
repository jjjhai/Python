# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:16:23 2018

@author: Administrator
"""

import re

"""
正则表达式中常用的字符含义（普通字符和11个元字符）：
普通字符：匹配自身   abc   abc
.：匹配任意除换行符"\n"外的字符   a.c   abc
\：转义字符，使后一个字符改变原来的意思   a\.c -> a.c   a\\c -> a\c
*：匹配前一个字符0或多次   abc* -> ab   abc* -> abccc
+：匹配前一个字符1次或无限次   abc+ -> abc   abc+ -> abccc
?：匹配前一个字符0次或1次   abc? -> ab   abc? -> abc
^：匹配字符串开头，在多行模式中匹配每一行的开头   ^abc -> abc
$：匹配字符串末尾，在多行模式中匹配每一行的末尾   abc$ ->	abc
|：匹配|左右表达式任意一个，从左到右匹配，如果|没有包括在()中，则它的范围是整个正则表达式   abc|def -> abcdef
{}：{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，{m,}则匹配m至无限次   ab{1,2}c -> abcabbc
[]：字符集，对应的位置可以是字符集中任意字符
    字符集中的字符可以逐个列出，也可以给出范围，如[abc]或[a-c]，[^abc]表示取反，即非abc
    所有特殊字符在字符集中都失去其原有的特殊含义。用\反斜杠转义恢复特殊字符的特殊含义
    a[bcd]e -> abe   a[acd]e -> ace   a[bcd]e -> ade
()：被括起来的表达式将作为分组，分组表达式作为一个整体，可以后接数量词。表达式中的|仅在该组中有效。	
    (abc){2}a(123|456)c -> abcabca456c  

"""

tt = "Tina is a good girl, she is cool, clever, and so on..."
# 编译正则表达式模式，返回一个对象的模式
rr = re.compile(r'\w*oo\w*')
# re.findall遍历匹配
print(rr.findall(tt))   #查找所有包含'oo'的单词  ['good', 'cool']

# 只匹配字符串的开始
print(re.match('com','comwww.runcomoob').group())   # com
print(re.match('com','Comwww.runcomoob',re.I).group())   # Com

# 只要找到第一个匹配然后返回
print(re.search('\dcom','www.4comrunoob.5com').group())   # 4com

# 按照能够匹配的子串将string分割后返回列表
print(re.split('\d+','one1two2three3four4five5'))   # ['one', 'two', 'three', 'four', 'five', '']

# 替换string中每一个匹配的子串后返回替换后的字符串（最后一个参数是替换个数）
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '-', text, 2))   # JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...

# 返回替换次数
print(re.sub("g.t","have",'I get A,  I got B ,I gut C'))   # I have A,  I have B ,I have C
print(re.subn("g.t","have",'I get A,  I got B ,I gut C'))   # ('I have A,  I have B ,I have C', 3)