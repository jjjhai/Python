# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:31:55 2018

@author: Administrator
"""

import argparse

parser = argparse.ArgumentParser(description="")
#定位参数，不需要加-
parser.add_argument("pr", help="print the string you use here")
parser.add_argument("square", help="display a square of a given number",
                    type=int)

#可选参数，-指定的短参数，--指定的长参数
#需要指定参数值：python argparse.py -v 4
parser.add_argument("-v", "--verbosity", help="increase output verbosity")

#不需要指定参数值：python argparse.py -v，此时verbose值为True和False
#parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

#可选值choices

#parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")

#count:当-vvv或者-v -v -v时候返回3, default参数默认值
parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")


#互斥参数，只能用其中一个参数
#group = parser.add_mutually_exclusive_group()
#group.add_argument("-v", "--verbose", action="store_true")
#group.add_argument("-q", "--quiet", action="store_true")


args = parser.parse_args()
#python argparse.py abc 4
print(args.pr, args.square**2)

if args.verbosity:
    print("verbosity turned on", args.verbosity)