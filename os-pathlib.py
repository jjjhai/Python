# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:58:14 2018

@author: Administrator
"""

import os
import pathlib
#判断文件是否存在
print(os.path.exists('datetime.py'))

print(os.path.exists('datetimes.py'))

print(os.path.isfile('datetime.py'))

#判断文件夹是否存在
print(os.path.exists('__pycache__'))

print(os.path.exists('__pycaches__'))

#判断文件是否可做读写操作
"""
os.F_OK: 检查文件是否存在
os.R_OK: 检查文件是否可读
os.W_OK: 检查文件是否可以写入
os.X_OK: 检查文件是否可以执行
"""
if os.access("datetime.py", os.F_OK):
    print("Given file path is exist.")

if os.access("datetime.py", os.R_OK):
    print("File is accessible to read")

if os.access("datetime.py", os.W_OK):
    print("File is accessible to write")

if os.access("datetime.py", os.X_OK):
    print("File is accessible to execute")


try:
    f = open("datetime.py")
    f.close()

except FileNotFoundError:
    print("File is not found.")

except IOError:
    print("You don't have permission to access this file.")
    
#检查路径是否存在
path = pathlib.Path("datetime.py")
print(path.exists())

#检查路径是否是文件
path = pathlib.Path("__pycache__")
print(path.is_file())

