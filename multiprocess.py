# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:48:10 2018

@author: Administrator
"""

import multiprocessing as mp
import threading
import time
import os

lock = threading.Lock()

def func():
    time.sleep(1)
    proc = mp.current_process()
    print(proc.name, proc.pid)
    
    
if __name__ == '__main__':
    sub_proc = mp.Process(target=func, args=())
    sub_proc.start()
    sub_proc.join()
    proc = mp.current_process()
    print(proc.name, proc.pid)
    
        
    
        
    