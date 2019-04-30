# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:05:54 2018

@author: Administrator
"""

import random

# 返回[0,1)实数
print(random.random())

# 返回[50,100]范围内实数
print(random.uniform(50,100))

print(random.randint(1,100))

print(random.randrange(10,100,2))
print(random.choice(range(10,100,2)))

print(random.choice(("stone", "scissors", "paper")))

#打乱序列
poker = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(poker)
print(poker)

#从指定序列中随机获取k个元素作为一个片段返回
print(random.sample(poker,5)) 