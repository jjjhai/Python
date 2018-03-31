# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:32:53 2018

@author: Administrator
"""

#hypot计算直角三角形斜边
from math import hypot
from random import random
import time

#multiprocessing的dummy包是对多线程的一个封装
from multiprocessing.dummy import Poolt 
from multiprocessing import Pool

import gevent
#import eventlet
#SCOOP
#from scoop import futures
#Asyncoro
#import asyncoro

#通过概念计算圆周率
def test(tries):
    return sum(hypot(random(), random()) < 1 for _ in range(tries))


#非并发
def calcPi(nbFutures, tries):
    ts = time.time()
    #[tries]*nbFutures生成列表包含nbFutures相同的tries
    result = map(test, [tries]*nbFutures)
    ret = 4. * sum(result) / float(nbFutures * tries)
    span = time.time() - ts
    print("time spend ", span)
    return ret


#print(calcPi(3000,4000))

#多线程
def calcPiThread(nbFutures, tries):
    ts = time.time()
    p = Poolt(1)
    result = p.map(test, [tries] * nbFutures)
    ret = 4. * sum(result) / float(nbFutures * tries)
    span = time.time() - ts
    print("time spend ", span)
    return ret

#多进程
def calcPiProcess(nbFutures, tries):
    ts = time.time()
    p = Pool(5)
    result = p.map(test, [tries] * nbFutures)
    ret = 4. * sum(result) / float(nbFutures * tries)
    span = time.time() - ts
    print("time spend ", span)
    return ret


#gevent伪进程
def calcPiGevent(nbFutures, tries):
    ts = time.time()
    jobs = [gevent.spawn(test, t) for t in [tries] * nbFutures]
    gevent.joinall(jobs, timeout=2)
    ret = 4. * sum([job.value for job in jobs]) / float(nbFutures * tries)
    span = time.time() - ts
    print("time spend ", span)
    return ret    


#eventlet伪线程
"""
def calcPiEventlet(nbFutures, tries):
    ts = time.time()
    pool = eventlet.GreenPool()
    result = pool.imap(test, [tries] * nbFutures)
    ret = 4. * sum(result) / float(nbFutures * tries)
    span = time.time() - ts
    print("time spend ", span)
    return ret
"""

if __name__ == '__main__':
    print("pi = {}".format(calcPiGevent(3000, 4000)))

