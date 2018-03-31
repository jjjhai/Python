# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:43:11 2018

@author: Administrator
"""

import atexit
import time
import math

 
def microtime(get_as_float = False):
    if get_as_float:
        return time.time()
    else:
        return('%f %d' % math.modf(time.time()))

start_time = microtime(False)

@atexit.register
def shutdown():
    global start_time
    print("Execution took: {0} seconds".format(start_time))

#atexit.register(shutdown)